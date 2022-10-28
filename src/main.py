from src.Login_Interface_Python_Logic import login_interface
from src.db_functions import new_user_credentials
from src.daily_words import randomWordGenerator
from src.db_searched_words import add_searched_word, display_all_searched_words, delete_searched_words, clean_db_for_new_user
from src.api import show_word_and_definition
import schedule
import time

def set_reminder_time():

    reminderTime = input("Please enter the time you would like your daily reminder in 24hr format:")

    # Every day at 'reminderTime' time randomWordGenerator() is called.
    schedule.every().day.at("{}".format(reminderTime)).do(randomWordGenerator)
    schedule.every().day.at("{}".format(reminderTime)).do(continue_learning)
    print("Your reminder has been set")
    # Loop so that the scheduling task
    # keeps on running all time.
    #learn_words()
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)



def learn_words():
    start = input('Would you like to search your Schedule your words, Search your Dictionary, or View your Searched Words? (Schedule Word/Search Dictionary/View Searched Words) ').lower()
    if start == 'schedule word':
        set_reminder_time()

    elif start == 'search dictionary':
        search_words_in_dictionary()
        continue_learning()
    elif start == 'view searched words':
        display_all_searched_words()
        continue_learning()
    else:
        print('Please try again')
        continue_learning()


def search_words_in_dictionary():
    search_again = input('Would you like to continue searching your dictionary? (Yes/No) ').lower()
    if search_again == 'no':
        print('You are leaving your dictionary...')
        return
    elif search_again == 'yes':
        search = input('Please search for a word in your dictionary: ')
        show_word_and_definition(search)
        add_searched_word(search)
        search_words_in_dictionary()
    else:
        print('Please try again.')
        search_words_in_dictionary()

def continue_learning():
    cont_learning = input('Would you like to continue? (Yes/No) ').lower()
    if cont_learning == 'no':
        print('See you next time.')
        exit(0)
    elif cont_learning == 'yes':
        learn_words()
    else:
        print("Please type 'Yes' or 'No'")
        continue_learning()


def run():
    print('##################################')
    print('Hello, welcome to the Gift of Language')
    print('##################################')
    print()
    run_user_input()

def run_user_input():
    option = input("""Would you like to 
                            (1) Login as an existing user
                            (2) Register as a new user
                            Choice (1/2): """)
    if option == '1':
        if login_interface():
            print("Let's start learning")
            learn_words()

    elif option == '2':
        print('Please register adding the required information.')
        new_user_credentials()
        print("Congratulations! Registration completed.")
        delete_searched_words()
        clean_db_for_new_user()
        start = input('Would you like to log in with your new account to start learning? (Yes/No)')
        if start == 'Yes':
            login_interface()
            print("Let's start learning")
            learn_words()
        elif start == 'No':
            print('See you next time.')
        else:
            print('Please try again.')
            learn_words()
    else:
        print('Please try again. Please select one of the two options.')
        run_user_input()
if __name__ == '__main__':
    run()