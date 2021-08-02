import flask
import json
import requests

def queryForWord():
    
    word2index = None 
    wordIndex = None


    with open("word2index.json", "r") as w2i:
        word2index = json.load(w2i)

    with open("wordslist.json", "r") as wl:
        wordIndex = json.load(wl)
    
    print("input search word")
    searchWord = input()

    lower = max(0, word2index[searchWord] - 5)
    upper = min(len(word2index) - 1, word2index[searchWord] + 5)

    li = []

    for i in range(lower, upper + 1):
      li.append(wordIndex[i])

    return li

def print_wiki(li):
    #print wikipedia definitions from list words

    for word in li:
        contents = requests.get("http://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&exintro&titles=" + word + "&redirects=")
        contents_JSON = contents.json()
        for key in contents_JSON['query']['pages'].keys():
            print(contents_JSON['query']['pages'][key]['extract'].split(".")[0])

        print("\n" * 3)
def main():
    li = queryForWord()
    print_wiki(li)

if __name__ == "__main__":

    main()

