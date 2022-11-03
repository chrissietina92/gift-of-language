from src.login_interface_python_logic import login_interface
from src.db_functions import new_user_credentials
from src.daily_words import randomWordGenerator
from src.db_searched_words import add_searched_word, display_users_searched_word
from src.dictionary_api_functions import show_word_and_definition
import schedule
import time
import re


# Function takes in user input to set time for a word and its definition to be displayed
def set_reminder_time(userid):
    reminderTime = input("Please enter the time you would like your daily reminder in 24hr format:")
    regex = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
    pattern = re.compile(regex)
    # searching regex
    match = re.search(pattern, reminderTime)
    # validating conditions
    if match:
        schedule.every().day.at("{}".format(reminderTime)).do(randomWordGenerator)
        schedule.every().day.at("{}".format(reminderTime)).do(continue_learning, userid)
        print("Your reminder has been set")

        # While loop so that the daily scheduling runs continuously
        # keeps on running all time.
        while True:
            # Checks whether a scheduled task
            # is pending to run or not
            schedule.run_pending()
            time.sleep(1)
    else:
        print('Please enter the right format of the time HH:MM')
        set_reminder_time(userid)


# Function takes in user input to let the user choose how the would like to proceed after logging in
def learn_words(userid):
    start = input('Would you like to search your Schedule your words, Search your Dictionary, or View your Searched Words? (Schedule Word/Search Dictionary/View Searched Words) ').lower()
    if start == 'schedule word':
        set_reminder_time(userid)

    elif start == 'search dictionary':
        search_words_in_dictionary(userid)
        continue_learning(userid)
    elif start == 'view searched words':
        list_of_searched_words = display_users_searched_word(userid)
        print("")
        print("SEARCHED WORDS:")
        for word in list_of_searched_words:
            print("{}: {}".format(word[0], word[1]))
        print("")
        continue_learning(userid)
    else:
        print('Please try again')
        continue_learning(userid)

# Function takes in user input to search for a word and it's definition from the API
def search_words_in_dictionary(userid):
    search_again = input('Would you like to continue searching your dictionary? (Yes/No) ').lower()
    if search_again == 'no':
        print('You are leaving your dictionary...')
        return
    elif search_again == 'yes':
        search = input('Please search for a word in your dictionary: ')
        show_word_and_definition(search)
        add_searched_word(search, userid)
        search_words_in_dictionary(userid)
    else:
        print('Please try again.')
        search_words_in_dictionary(userid) #JACK SAID TO GET RID OF THESE RECURSION, MAYBE JUST EXIT PROGRAMME

# Function takes in user input to decide whether they would like to exit their current option or continue learning via the app
def continue_learning(userid):
    cont_learning = input('Would you like to continue? (Yes/No) ').lower()
    if cont_learning == 'no':
        print('See you next time.')
        exit(0)
    elif cont_learning == 'yes':
        learn_words(userid)
    else:
        print("Please type 'Yes' or 'No'")
        continue_learning(userid) #JACK SAID TO GET RID OF THESE RECURSION, MAYBE JUST EXIT PROGRAMME


def run():
    print('##################################')
    print('Hello, welcome to the Gift of Language')
    print('##################################')
    print()
    run_user_input()


# This is the first initial function that is ran to start the flow of the entire program/app
def run_user_input():
    option = input("""Would you like to 
                            (1) Login as an existing user
                            (2) Register as a new user
                            Choice (1/2): """)
    if option == '1':
        login = login_interface()
        if login[0]:
            print("Let's start learning")
            userid = login[1]
            learn_words(userid)

    elif option == '2':
        print('Please register adding the required information.')
        duplicate = new_user_credentials()
        if duplicate:
            start = input('A User already exists with these details, would you like to log in? (Yes/No)')
        else:
            print("Congratulations! Registration completed.")
            start = input('Would you like to log in with your new account to start learning? (Yes/No)')
        if start.title() == 'Yes':
            login = login_interface()
            if login[0]:
                print("Let's start learning")
                learn_words(login[1])
            else:
                print('Sorry your log in details were wrong, goodbye')
                return
        elif start.title() == 'No':
            print('See you next time.')
        else:
            print('That was an incorrect input, goodbye')

    else:
        print('Please try again. Please select one of the two options.')
        run_user_input()

if __name__ == '__main__':
    run()