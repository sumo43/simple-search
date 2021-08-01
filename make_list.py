import gensim
import numpy as np
from sklearn.manifold import TSNE
from os import path

# number of words to use in search
N = 1000
data_path = "data/"

def generate_wordsList(model, topNWords):
    
    arr = np.empty((0,300), dtype='f')
        
    # add the vector for each of the closest words to the array
    for word in topNWords:
        word_vector = model.get_vector(word)
        arr = np.append(arr, np.array([word_vector]), axis=0)
        
    
    # find tsne coords for 2 dimensions
    tsne = TSNE(n_components=1, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)

    li = Y[:, 0]

    return li



def main():
    
    print("using word count: ", N)
    #load the model from gensim
    print("loading word2vec vectors...")
    model = gensim.models.KeyedVectors.load_word2vec_format(path.join(data_path, 'GoogleNews-vectors-negative300.bin.gz'), binary=True)

    #make the vocab
    vocab = model.index_to_key

    # get top N words from vocab
    topNWords = vocab[1:N+1]

    # generate list of words
    print("generating words list...")
    li = generate_wordsList(model, topNWords)

    word2vec = dict()

    for i in range(len(topNWords)):
      word2vec[topNWords[i]] = li[i]

    # get an ordered list of the words based on their 1-d representation

    wordIndex = [x for x, y in sorted(zip(topNWords, li), key=lambda x: x[1])]

    word2index = dict()

    for i in range(len(wordIndex)):
      word2index[wordIndex[i]] = i


    print("input search word")
    searchWord = input()

    lower = max(0, word2index[searchWord] - 5)
    upper = min(len(word2index) - 1, word2index[searchWord] + 5)

    for i in range(lower, upper + 1):
      print(wordIndex[i])

if __name__ == "__main__":
    main()

