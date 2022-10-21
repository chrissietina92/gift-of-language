import requests

def get_definition(word):
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = requests.get(dictionary_url)
    print(response.status_code)
    word_data = response.json()

    # writing the definition of the word and its examples to a file
    with open('Dictionary.txt', 'w') as dictionary:

        for i in word_data:
            for j in i['meanings']:
                for k in j['definitions']:
                    # print(k)
                    definition = k['definition']
                    dictionary.writelines('\nDefinition: ' + definition)
                    if 'example' in k:
                        dictionary.writelines('\nExample: ' + k['example'])
                    dictionary.writelines('\n')


# example looking up the word 'hello' on the API
term = 'hello'
get_definition(term)
