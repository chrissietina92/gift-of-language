import requests
import random

# Documentation:
# I'm using this manual method below for the random word generator based on the words in our chosen api
# instead of using the random words library as :
# 1. A lot of the words don't exist in the api we are using so the definition and examples etc can't be searched
# 2. The words it generates are extremely advanced english that I don't even know myself and aren't commonly used in day too day speaking

# GENERATING THE RANDOM WORD FOR USERS DAILY WORD
def randomWordGenerator():
    # Converting the text file of the dictionary words into a list of strings
    with open("../docs/english.txt", encoding="utf8") as wordDictionary:
        wordDictionaryList = []  # the wordDictionary in list form
        for line in wordDictionary:
            wordDictionaryList.append(line.strip())
            #  print(wordDictionaryList)    # the wordDictionary in list form
            #  print(wordDictionaryList)    # the wordDictionary in list form

    # Total number of dictionary words
    dictionaryLength = len(wordDictionaryList)
    #  print(dictionaryLength)

    # Generates a random number within the range of the index for the list of dictionary words
    randomDictIndex = random.randint(0, dictionaryLength - 1)
    #  print("RANDOM DICTIONARY INDEX: " , randomDictIndex)

    # Getting our random word
    randomWord = wordDictionaryList[randomDictIndex]
    #  print("RANDOM WORD: " , randomWord)

    return searchAPIForRandomWord(randomWord)



#  SEARCHING THE API WITH A RANDOMLY GENERATED WORD
def searchAPIForRandomWord(randomWord):
    # CONNECTING TO AN API TO SEARCH WITH THE RANDOM WORD AND PRINT ITS NAME AND DEFINITION
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(randomWord)

    response = requests.get(dictionary_url)
    # print(response.status_code)  #should be 200
    word_data = response.json()  # word_data is the API's list of dictionaries

    # printing the name and definition of the word from its dictionary
    for dictionary in word_data:
        print("Word: " + dictionary['word'])  # print the value of the word key
        print("Definition: " + dictionary['meanings'][0]['definitions'][0]['definition'])
        # print("Definition: " + dictionary['meanings'][0]['definitions'][0]['example'])

    return "Word: {}".format(word_data[0]['word']), "Definition: {}".format(word_data[0]['meanings'][0]['definitions'][0]['definition'])


