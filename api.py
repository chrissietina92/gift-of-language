import requests

def get_definition(word):
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = requests.get(dictionary_url)
    # print(response.status_code)
    word_data = response.json()

    return word_data[0]['meanings'][0]['definitions'][0]['definition']

def show_word_and_definition(word):
    print('The word is: {}'.format(word))
    print('The definition is: {}'.format(get_definition(word)))