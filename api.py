import requests


def get_definition(word):
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = requests.get(dictionary_url)
    # print(response.status_code)
    word_data = response.json()

    # writing the word and its definition to a file
    with open('SearchedWords.txt', 'w') as SearchedWords:

        # word_data is in a form of a list of dictionaries.
        # within each index, the values in the dictionaries are another list of dictionaries

        for dictionary in word_data:  # i is each index in word_data
            SearchedWords.writelines("\n\nWord: {}".format(word.capitalize()))
            SearchedWords.writelines("\nDefinition: " + dictionary['meanings'][0]['definitions'][0]['definition'])
            #SearchedWords.writelines("\nExample: " + dictionary['meanings'][0]['definitions'][0]['example'])


# example looking up the word 'House' on the API
get_definition('house')