from .utils import *
from .models import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import innvestigate
import random

def truncate_colormap_center(cmap, minval=0.0, maxval=1.0, centerval = 0.5, centertrunc = 0.0,  n=256):
    """
        ### To cut the sides of the cmap
            minval: minimum value of the cmap (0.0 by default)
            maxval: maximum value of the cmap (1.0 by default)
        ### To cut the center of the cmap
            centerval: center of the cmap (0.5 by default)
            centertrunc: portion of center to cut (0.0, nothing, by default)
    """
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f},{c:.2f},{d:.2f})'.format(n=cmap.name, a=minval, b=centerval-centertrunc/2, c=centerval+centertrunc/2, d=maxval),
        np.concatenate( [
            cmap(np.linspace(minval, centerval-centertrunc/2, int(n*(centerval-centertrunc/2)/(1.0-centertrunc)))), 
            cmap(np.linspace(centerval+centertrunc/2, maxval, int(n*(maxval-centerval-centertrunc/2)/(1.0-centertrunc))))
        ], axis=0)
    )
    return new_cmap

CMAP = {
        'white': truncate_colormap_center(plt.get_cmap('twilight_shifted'), centertrunc = 0.25, centerval = .48),
        'black': truncate_colormap_center(plt.get_cmap('Blues'), minval = 0.0, maxval = 0.75)
    }

# Feature extraction part only
def get_feature_extraction_model_cnn(cnn_model, filter_list, embedding_dim, maxlen): # Start from embedded text input
    embedded_text_input = Input(shape=(maxlen, embedding_dim), name='embedded_text_input')   
    filters_fe = [Conv1D(f[0], f[1], activation='relu', weights = cnn_model.layers[2+idx].get_weights(), trainable = False)(embedded_text_input) for idx, f in enumerate(filter_list)]
    max_pools_fe = [GlobalMaxPool1D()(result) for result in filters_fe]
    concatenated_fe = concatenate(max_pools_fe, axis=-1)

    fe_model = Model(embedded_text_input, concatenated_fe)
    fe_model.summary()
    return fe_model

# Find important n-grams for each feature

def find_evidence_from_relevance(X_vector, relevance_vector, index2word):
    """
    Given an input vector (a list of word indices) and a vector of relevance scores
    Return (important_evidence_ngram, evidence_scores) 
    """
    # This implementation is for CNN, max-pooling only
    scores = sum(relevance_vector)
    ngram = decode_sequence(index2word, X_vector[relevance_vector.nonzero()], pad = True)
    return (ngram, scores)

def summarize_ngram_list(alist, expected_space, score):
    """
    This function is for CNN, max-pooling only
    Given a list of all ngrams with the same relevance score
    Find the count and the representative string
    """
    count = len(alist)
    if alist[0].count(' ') <= expected_space:
        rep = alist[0]
    else:
        rep = ' '.join(alist[0].split(' ')[0:expected_space+1])
    if not all([s.startswith(rep) for s in alist]):
        print(f'Warning: cannot summarize different ngrams {alist}, {score}')
    return count, rep

def get_wordcloud(ngrams_stat, background_color = 'black', show = True):
    frequencies = {entry['ngram']:entry['score'] for entry in ngrams_stat}
    wordcloud = WordCloud(width=600, height=300, background_color=background_color, colormap=CMAP[background_color]).generate_from_frequencies(frequencies)
    if show:
        plt.rcParams['figure.figsize'] = [14, 7]
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
    return wordcloud

def get_window_size_from_feature_index(feature_idx, filters):
    assert feature_idx >= 0 and feature_idx < num_all_filters(filters)
    cumulative_idx = 0
    for p in filters:
        cumulative_idx += p[0]
        if feature_idx < cumulative_idx:
            return p[1]

def generate_wordclouds(model, X_train, settings, max_examples = 2000):
    model_arch = settings['model_arch']
    FILTERS = settings['filters']
    MAXLEN = settings['maxlen']
    result_path = settings['result_path']
    index2word = settings['index2word']
    EMBEDDING_DIM = settings['embedding_dim']
    BATCH_SIZE = settings['batch_size']

    if model_arch == 'CNN':
        # Create an analyzer
        feature_extraction_model = get_feature_extraction_model_cnn(model, FILTERS, EMBEDDING_DIM, MAXLEN)
        analyzer = innvestigate.create_analyzer('lrp.epsilon', feature_extraction_model, neuron_selection_mode="index")        

        # Input word indices --> Embedding matrix of shape (Num_examples, max_len, embedding_dim)    
        embeddings_func = K.function([model.layers[0].input],[model.layers[1].output])
        X_train_emb = batch_processing(embeddings_func, [X_train[:min(max_examples, len(X_train))]], batch_size = BATCH_SIZE)[0]

        # Find important n-grams (i.e., evidence, selected n-grams) for each feature
        top_ngrams_of_features = dict()  # For intermediate results 
        ngrams_stat_of_features = [[] for i in range(num_all_filters(FILTERS))]     # For final results
        for feature_idx in tqdm(range(num_all_filters(FILTERS))):
            top_ngrams_of_features[feature_idx] = dict() # key = score, value = list of ngrams holding the score
            relevance_scores = np.array([]).reshape(0, len(X_train[0]))
            i = 0
            while i < len(X_train_emb):
                relevance_scores = np.vstack([relevance_scores, analyzer.analyze(X_train_emb[i:min(i+100, len(X_train_emb))], feature_idx).sum(axis = -1)]) # Shape: (Num_examples, max_len)
                i += 100
            # Find the important n-gram for each example and save it to top_ngrams_of_features
            for example_idx, relevance_vector in enumerate(relevance_scores):
                ngram, score = find_evidence_from_relevance(X_train[example_idx], relevance_vector, index2word) # (ngram, the_score)
                if score in top_ngrams_of_features[feature_idx]:
                    top_ngrams_of_features[feature_idx][score].append(ngram)
                else:
                    top_ngrams_of_features[feature_idx][score] = [ngram]
            
            # Summarize n-grams stat (e.g., merge duplicate n-grams)
            for score, ngrams_list in top_ngrams_of_features[feature_idx].items():
                count, rep = summarize_ngram_list(ngrams_list, get_window_size_from_feature_index(feature_idx, FILTERS) - 1, score)
                ngrams_stat_of_features[feature_idx].append({'ngram': rep, 'score': score, 'count': count})
            ngrams_stat_of_features[feature_idx].sort(key=lambda x: x['score'], reverse = True) # sort by evidence scores
            
        # Generate wordclouds
        all_wordclouds = [get_wordcloud(ngrams_stat_of_features[feature_idx], show = False) for feature_idx in tqdm(range(num_all_filters(FILTERS)))]
        pickle.dump(all_wordclouds, open(result_path + f"all_wordclouds.pickle", "wb"))
        
        # Save wordcloud figures
        if not os.path.exists(result_path + 'wordclouds'):
            os.makedirs(result_path + 'wordclouds')
        for feature_idx, wordcloud in enumerate(all_wordclouds):
            plt.rcParams['figure.figsize'] = [14, 7]
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.savefig(result_path + f'wordclouds/Wordcloud_Feature{feature_idx}.png')
            plt.close()

    else:
        assert False, f"Unsupported model architecture {model_arch}"

    return all_wordclouds

def visualize_weights(W, feature_idx, class_names, show = True):
    max_abs_W = np.max(np.abs(W)) + 0.1 # For plotting
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 2)
    ax.barh(class_names, W[feature_idx], color = ['green' if w >= 0 else 'red' for w in W[feature_idx]])
    ax.set_xlim((-max_abs_W, max_abs_W))
    ax.set_yticks(range(len(class_names)))
    ax.set_yticklabels(class_names)
    ax.yaxis.tick_right()
    ax.invert_yaxis()
    ax.set_xlabel('Weights')
    ax.set_title(f'Feature {feature_idx}')
    for i, v in enumerate(W[feature_idx]):
        if v >= 0:
            ax.text(v + 0.01, i + .05, '%.4f'%(v), color='black')
        else:
            ax.text(v - 0.13, i + .05, '%.4f'%(v), color='black')
    if show:
        plt.show()
    return ax

def generate_weightplots(model, result_path, class_names):
    W = model.layers[-1].get_weights()[0]
    if not os.path.exists(result_path + 'featureweights'):
        os.makedirs(result_path + 'featureweights')
    for feature_idx in range(num_all_filters(FILTERS)):
        weight_plot = visualize_weights(W, feature_idx, class_names, show = False)
        plt.savefig(result_path + f'featureweights/WeightsFeature{feature_idx}.png')
        plt.close()