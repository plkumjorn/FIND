import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import spacy
from tqdm import tqdm 
from keras.preprocessing.sequence import pad_sequences

nlp = spacy.load('en')
tokenizer = spacy.load('en', disable = ['tagger', 'parser', 'ner', 'textcat']) # Use only tokenizer

def get_glove_dict(glove_path):
    """
    Return a dictionary of glove word embeddings
    E.g., glove['happy'] = np.array([0.25, -0.11, ...])
    """
    # Thanks to Karishma Malkan (from https://stackoverflow.com/questions/37793118/load-pretrained-glove-vectors-in-python)
    print("Loading Glove Model")
    f = open(glove_path,'r', encoding = 'utf-8')
    model = {}
    for line in tqdm(f):
        try:
            splitLine = line.split()
            model[splitLine[0]] = np.array([float(val) for val in splitLine[1:]])
        except:
            continue
    print("Done.",len(model)," words loaded!")
    return model

def get_embedding_matrix(glove_path, embedding_dim, pad_initialisation = "uniform"):
    """
    Return a numpy embedding matrix of shape (vocab_size, embedding_dim)
    together with vocab_size, index2word, word2index
    """
    # Get glove dictionary
    glove = get_glove_dict(glove_path)
    
    # Create index-word mapping
    index2word = ['PAD','UNK'] + list(glove.keys())
    word2index = dict([(w, idx) for idx, w in enumerate(index2word)])
    index2word = dict([(idx, w) for idx, w in enumerate(index2word)])
    
    # Initialise vectors for PAD and UNK
    mean_vector = np.mean(np.array(list(glove.values())), axis = 0)
    if pad_initialisation == "uniform":
        pad_vector = np.array(np.random.uniform(-1.0, 1.0, embedding_dim))
    elif pad_initialisation == "zeros":
        pad_vector = np.zeros(embedding_dim)
    else:
        assert False, "Invalid pad_initialisation"
    
    # Create the embedding matrix
    embedding_matrix = np.concatenate(([pad_vector, mean_vector], np.array([glove[index2word[idx]] for idx in range(2, len(index2word))])), axis = 0)
    vocab_size = len(index2word)
    return embedding_matrix, vocab_size, index2word, word2index

def get_doc_vector(text, vocab, word2index, maxlen):
    """
    Return a list of word indices given an input sentence (text).
    """
    tokens = tokenizer(text)
    vector = []
    for token in tokens:
        if token.text.lower() in vocab:
            vector.append(word2index[token.text.lower()])
        elif token.text.lower().strip() != '':
            vector.append(1) # UNK
        if len(vector) >= maxlen:
            break
    return vector

def get_data_matrix(textlist, word2index, maxlen, use_tqdm = True):
    """
    Return a matrix of padded examples with a shape of (num_examples, MAXLEN).
    """
    ans = []
    vocab = set(word2index.keys())
    textlist = tqdm(textlist) if use_tqdm else textlist
    for text in textlist:
        vector = get_doc_vector(text, vocab, word2index, maxlen)
        ans.append(vector)
    ans = np.array(ans)
    ans = pad_sequences(ans, maxlen, dtype='int32', padding='post', truncating='post', value=0.0)
    return ans  

def decode_sequence(index2word, seq, pad = False):
    """
    Translate a sequence of word indices to a decoded sentence.
    """
    if pad:
        return ' '.join([index2word[i] if i != 0 else '_' for i in seq])
    else:
        return ' '.join([index2word[i] for i in seq if i != 0])