from datetime import datetime
import requests
import random

#from #rebeccas pythonfile import login_interface


# Userdefined exception
class Value_not_in_twenty_four_hour(ValueError):
    # called if the time entered is not in 24hr time
    pass


def set_reminder_time():

    try:
        print("Please enter the time you would like your daily reminder in 24hr format.")
        reminderHour = int(input("Enter the Hour : "))
        reminderMin = int(input("Enter the Minute : "))

        if 24 < reminderHour < 1 and 60 < reminderMin < 1:
            raise Value_not_in_twenty_four_hour
    
    except Value_not_in_twenty_four_hour:
        print("Please enter your reminder time in 24hr format.")

    else:          
        if reminderHour == datetime.datetime.now().hour and reminderMin == datetime.now().minute: #if the current time is equal to the reminder time
            randomWordGenerator()
              



"""if login_interface() == True:  # if user successfully logs in
    set_reminder_time()        # let them set a time reminder for their random words
    
"""

# GENERATING THE RANDOM WORD FOR USERS DAILY WORD
def randomWordGenerator():    

    # Converting the text file of the dictionary words into a list of strings
    with open("daily_word_automation\english.txt", encoding="utf8") as wordDictionary:
        wordDictionaryList = []       # the wordDictionary in list form
        for line in wordDictionary:
            wordDictionaryList.append(line.strip)
        #print(wordDictionaryList)    # the wordDictionary in list form

    # Total number of dictionary words
    dictionaryLength = len(wordDictionaryList)
    #print(dictionaryLength)  

    # generates a random number within the range of the index for the list of dictionary words
    randomDictIndex = random.randint(0,dictionaryLength-1) 
    #print(randomDictIndex)  

    # getting our random word
    randomWord = wordDictionaryList[int(randomDictIndex)]
    
    




def searchAPIForRandomWord(randomWord):

    # CONNECTING TO AN API TO SEARCH WITH THE RANDOM WORD AND PRINT ITS NAME AND DEFINITION
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(randomWord)

    response = requests.get(dictionary_url)
    #print(response.status_code)  #should be 200
    word_data = response.json()    # word_data is the API's list of dictionaries


    """
    Explanation for below code:
    Word data is a list
    'dictionary' are the dictionaries in this list
    the value of the meanings key is a list
    the first entry of that list is a dictionary
    definitions is a key inside that dictionary, the value of which is a list
    there is only one entry in that list, another dictionary
    definition is the key whose value is what you are wanting to print.
    
    So you have a string (the thing you are printing) inside a dictionary,
    which is inside a list (definitions), which is inside a dictionary, 
    which is inside a list (meanings) which is inside a dictionary,
    which is inside a list.
    
    """

    # printing the name and definition of the word from its dictionary
    for dictionary in word_data:    
        print(dictionary['word'])   # print the value of the word key
        print(dictionary['meanings'][0]['definitions'][0]['definition'])  


searchAPIForRandomWord("cat")





