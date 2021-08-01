





def queryForWord():

    print("input search word")
    searchWord = input()

    lower = max(0, word2index[searchWord] - 5)
    upper = min(len(word2index) - 1, word2index[searchWord] + 5)

    for i in range(lower, upper + 1):
      print(wordIndex[i])

