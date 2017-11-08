TAG_PAD = '<PAD>'
TAG_BOS = '<BOS>'
TAG_EOS = '<EOS>'
TAG_UNK = '<UNK>'

TAGS = {'<PAD>': 0, '<EOS>': 1, '<UNK>': 2, '<BOS>': 3 }

MAX_VOCABULARY = int(2193)
MAX_INPUT_LENGTH = int(15)
MAX_OUTPUT_LENGTH = int(15)  

# define some constants (including hyperparameters)
WORD_EMBEDDING_SIZE = int(100) 
SENTENCE_EMBEDDING_SIZE = int(300)
NUMBER_OF_LAYERS = 2 # how many layers of LSTM's we want for our decoder 

# *** file paths *** 
FILE_TRAINING_DATA = 'data/friends-final.txt'

FILE_TRAINING_DATA_EXTRACT = 'workingdata/friends_dialog_extract.pickle'

FILE_TRAINING_DATA_ENCODER_INPUTS = 'workingdata/friends_encoder_input.pickle'
FILE_TRAINING_DATA_DECODER_INPUTS = 'workingdata/friends_decoder_input.pickle'
FILE_VOCAB = 'workingdata/friends_vocab.pickle'

FILE_EMBEDDING_MATRIX = 'workingdata/friends_embedding_matrix.npy'
FILE_WEIGHTS = 'localdata/friends_weights.h5'

GLOVE_DIR = 'localdata/glove.6B/'