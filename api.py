import requests


def get_definition(word):
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = requests.get(dictionary_url)
    # print(response.status_code)
    word_data = response.json()

    return "Word: {}".format(word_data[0]['word']), "Definition: {}".format(word_data[0]['meanings'][0]['definitions'][0]['definition'])

# example looking up the word 'House' on the API
print(get_definition('house'))