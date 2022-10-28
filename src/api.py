import requests

def get_definition(word):
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = requests.get(dictionary_url)
    # print(response.status_code)
    word_data = response.json()
    try:
        definition = word_data[0]['meanings'][0]['definitions'][0]['definition']
    except Exception:
        return 'This word does not exist in the dictionary.'
    else:
        return definition


def show_word_and_definition(word):
    if get_definition(word) == 'This word does not exist in the dictionary.':
        print('This word does not exist in the dictionary.')
        # return 'This word does not exist in the dictionary.'
    else:
        print('The word is: {}'.format(word))
        print('The definition is: {}'.format(get_definition(word)))
        # return """The definition of {} is: {}""".format(word, get_definition(word))


