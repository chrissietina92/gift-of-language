import requests

def get_definition(word):
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)

    response = requests.get(dictionary_url)
    print(response.status_code)
    word_data = response.json()

    # writing the definition of the word and its examples to a file
    with open('Dictionary.txt', 'w') as dictionary:

        # word_data is in a form of a list of dictionaries.
        # within each index, the values in the dictionaries are another list of dictionaries
        # using a nested for loop to obtain the data.

        for i in word_data:  # i is each index in word_data
            dictionary.writelines('Definition for the word {}\n'.format(word.capitalize()))

            for j in i['meanings']:  # j is the value for the key 'meanings' in i

                for k in j['definitions']:  # k is the value for the key 'definitions' in j
                    definition = k['definition']
                    dictionary.writelines('\nDefinition: ' + definition)
                    if 'example' in k:
                        dictionary.writelines('\nExample: ' + k['example'])
                    dictionary.writelines('\n')


# example looking up the word 'hello' on the API
term = 'hello'
get_definition(term)
