import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import string, keras, spacy, pickle, json, math, random, os
import numpy as np
from tqdm import tqdm
import tensorflow as tf
import pandas as pd
from collections import Counter
from keras.utils.np_utils import to_categorical
os.environ['PYTHONHASHSEED'] = '0'

from keras import backend as K
from keras.models import Sequential, Model 
from keras.layers import Dense, Embedding, Conv1D, GlobalMaxPool1D, Input, concatenate
from keras.layers import Layer, InputSpec
from keras.callbacks import ModelCheckpoint, EarlyStopping


# Special layer: Masked dense layer
class MaskedDense(Layer):

    def __init__(self, units, activation=None, use_bias=True, **kwargs):
        self.units = units
        self.activation = keras.activations.get(activation)
        self.use_bias = use_bias
        self.kernel_initializer = keras.initializers.glorot_uniform()
        self.bias_initializer = keras.initializers.Zeros()
        self.mask_initializer = keras.initializers.Ones()
        super(MaskedDense, self).__init__(**kwargs)

    def build(self, input_shape):
        # Create a trainable weight variable for this layer.
        input_dim = input_shape[-1]

        self.kernel = self.add_weight(shape=(input_dim, self.units),
                                      initializer=self.kernel_initializer,
                                      name='kernel')
        
        # The mask is not trainable
        self.mask = self.add_weight(shape=(input_dim, self.units),
                                      initializer=self.mask_initializer,
                                      trainable=False,
                                      name='mask')
        
        if self.use_bias:
            self.bias = self.add_weight(shape=(self.units,),
                                        initializer=self.bias_initializer,
                                        name='bias')
        else:
            self.bias = None
        self.input_spec = InputSpec(min_ndim=2, axes={-1: input_dim})
        self.built = True
        super(MaskedDense, self).build(input_shape)  # Be sure to call this at the end

    def call(self, inputs):
        output = K.dot(inputs, self.kernel * self.mask)
        if self.use_bias:
            output = K.bias_add(output, self.bias, data_format='channels_last')
        if self.activation is not None:
            output = self.activation(output)
        return output

    def compute_output_shape(self, input_shape):
        assert input_shape and len(input_shape) >= 2
        assert input_shape[-1]
        output_shape = list(input_shape)
        output_shape[-1] = self.units
        return tuple(output_shape)
    
    def set_mask(self, value, feature_idx, class_idx = None):
        """
        Set the mask of [feature_idx, class_idx] to a value.
        feature_idx: index of the feature
        class_idx: index of the class (or a list of indices). None means setting the value to all the classes
        value: the value to set
        """
        weights = K.get_value(self.mask)
        assert feature_idx >= 0 and feature_idx < weights.shape[0], f"Feature index out of bound [0, ..., {weights.shape[0]-1}] -- {feature_idx} given"
        if class_idx is not None:
            if isinstance(class_idx, list):
                for idx in class_idx:
                    assert idx >= 0 and idx < weights.shape[1], f"Class index out of bound [0, ..., {weights.shape[1]-1}] -- {idx} given"
                    weights[feature_idx,idx] = value
            elif isinstance(class_idx, int):
                idx = class_idx
                assert idx >= 0 and idx < weights.shape[1], f"Class index out of bound [0, ..., {weights.shape[1]-1}] -- {idx} given"
                weights[feature_idx,idx] = value
        else:
            weights[feature_idx,:] = value
        K.set_value(self.mask, weights)
        
    def disable_mask(self, feature_idx, class_idx = None):
        self.set_mask(value = 0, feature_idx = feature_idx, class_idx = class_idx)
        
    def enable_mask(self, feature_idx, class_idx = None):
        self.set_mask(value = 1, feature_idx = feature_idx, class_idx = class_idx)
        
    def get_masked_weights(self):
        return K.get_value(self.mask) * K.get_value(self.kernel)

# For adding binary features
class WordMatching(Layer):

    def __init__(self, units, **kwargs):
        self.units = units
        self.indices_initializer = keras.initializers.Zeros()
        super(WordMatching, self).__init__(**kwargs)

    def build(self, input_shape):
        # Create a trainable weight variable for this layer.
        input_dim = input_shape[-1]
        
        # The specified indices are not trainable
        self.indices = self.add_weight(shape=(self.units,),
                                      initializer=self.indices_initializer,
                                      trainable=False,
                                      name='indices')
        
        self.input_spec = InputSpec(min_ndim=2, axes={-1: input_dim})
        self.built = True
        super(WordMatching, self).build(input_shape)  # Be sure to call this at the end

    def call(self, inputs):
        X = K.expand_dims(inputs, -1)
        indices = K.cast(self.indices, 'int32')
        output = K.equal(X, indices)
        output = K.any(output, -2)
        output = K.cast(output, 'float32')
        return output

    def compute_output_shape(self, input_shape):
        assert input_shape and len(input_shape) >= 2
        output_shape = list(input_shape)
        output_shape[-1] = self.units
        return tuple(output_shape)

# Model Training
def model_train(model, bestmodel_path, X_train, y_train, X_validate, y_validate, batch_size, epochs = 100):
    # To one-hot encoding
    y_train_onehot, y_validate_onehot = to_categorical(y_train), to_categorical(y_validate)

    # Define four callbacks to use
    checkpointer = ModelCheckpoint(filepath=bestmodel_path, verbose=1, save_best_only=True)
    early_stopping = EarlyStopping(monitor='val_loss', patience=3)

    # Train the model
    history = model.fit(X_train, y_train_onehot, verbose = 2, epochs=epochs, batch_size=batch_size, callbacks=[checkpointer, early_stopping], validation_data=(X_validate, y_validate_onehot))

    # Load the best weights to the model
    model.load_weights(bestmodel_path)
    
    return history

def batch_processing(kfunc, input, batch_size):
    """
    K.function can handle limited numbers of examples at a time. This function enables batch processing for K.function.
    """
    num_total = len(input[0])
    num_batches = math.ceil(num_total / batch_size)
    print(f'Num batches: {num_batches}')
    output = None
    for b in tqdm(range(num_batches)):
        this_input = [i[batch_size*b : min(len(i), batch_size*(b+1))] for i in input]
        this_output = kfunc(this_input)
        if output is None:
            output = this_output
        else:
            for i in range(len(output)):
                output[i] = np.concatenate((output[i], this_output[i]), axis = 0)
    return output

def get_CNN_model(vocab_size, embedding_dim, embedding_matrix, maxlen, target_names, filters,
                 trainable_embedding = False,
                 trainable_filters = True):
    
    text_input = Input(shape=(None,), dtype='int32')
    embedded_text = Embedding(vocab_size, embedding_dim, 
                               weights=[embedding_matrix], 
                               input_length=maxlen, 
                               trainable=trainable_embedding)(text_input)
    
    filter_layers = [Conv1D(f[0], f[1], activation='relu', trainable=trainable_filters)(embedded_text) for f in filters]
    max_pool_layers = [GlobalMaxPool1D()(result) for result in filter_layers]
            
    concatenated = concatenate(max_pool_layers,axis=-1)

    ans = MaskedDense(len(target_names), activation='softmax')(concatenated)

    model = Model(text_input, ans)
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.summary()
    return model

def num_all_filters(filter_list):
    """
    Example input: [(10, 2), (10, 3), (10, 4)]
    Example output: 30
    """
    return sum([t[0] for t in filter_list])

def get_kernel_index(filter_idx, filter_list):
    """
    Input: a filter_idx
    Output: the corresponding kernel index (layer index) and the offset (the position in the layer)
    """
    if filter_idx < 0 or filter_idx >= num_all_filters(filter_list):
        assert False, f"Invalid filter index {filter_idx} -- Only filter indices in the range [0, {num_all_filters(filter_list)-1}] are valid."
    
    kernel_idx = -1
    max_filter_idx = -1
    for t in filter_list:
        kernel_idx += 1
        if filter_idx <= max_filter_idx + t[0]:
            ans = (kernel_idx, filter_idx - max_filter_idx - 1)
            return ans
        max_filter_idx += t[0]

