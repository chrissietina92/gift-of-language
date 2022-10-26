from Login_Interface_Python_Logic import existing_customer_check
from db_functions import new_user_credentials
from daily_words import randomWordGenerator
from db_searched_words import add_searched_word, display_all_searched_words, delete_searched_words_for_new_user, clean_db_for_new_user
from api import show_word_and_definition
import schedule
import time

def set_reminder_time():

    reminderTime = input("Please enter the time you would like your daily reminder in 24hr format:")

    # Every day at 'reminderTime' time randomWordGenerator() is called.
    schedule.every().day.at("{}".format(reminderTime)).do(randomWordGenerator)
    schedule.every().day.at("{}".format(reminderTime)).do(continue_learning)
    # Loop so that the scheduling task
    # keeps on running all time.
    #learn_words()
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)



def learn_words():
    start = input('Would you like to search your Schedule your words, Search your Dictionary, or View your Searched Words? (Schedule Word/Search Dictionary/View Searched Words) ')
    if start == 'Schedule Word':
        set_reminder_time()

    elif start == 'Search Dictionary':
        search_words_in_dictionary()
        continue_learning()
    elif start == 'View Searched Words':
        display_all_searched_words()
        continue_learning()
    else:
        print('Please try again')
        continue_learning()


def search_words_in_dictionary():
    search_again = input('Would you like to continue searching your dictionary? (Yes/No) ')
    if search_again == 'No':
        print('You are leaving your dictionary...')
        return
    else:
        search = input('Please search for a word in your dictionary: ')
        show_word_and_definition(search)
        add_searched_word(search)
    search_words_in_dictionary()

def continue_learning():
    cont_learning = input('Would you like to continue? (Yes/No) ')
    if cont_learning == 'No':
        print('See you next time.')
        exit(0)
    elif cont_learning == 'Yes':
        learn_words()


def run():
    print('##################################')
    print('Hello, welcome to the Gift of Language')
    print('##################################')
    print()
    option = int(input("""Would you like to 
                        (1) Login as an existing user
                        (2) Register as a new user
                        Choice (1/2): """))

    if option == 1:
        existing_customer_check()
        print("Let's start learning")
        learn_words()

    else:
        print('Please register adding the required information.')
        new_user_credentials()
        print("Congratulations! Registration completed.")
        delete_searched_words_for_new_user()
        clean_db_for_new_user()
        start = input('Would you like to log in with your new account to start learning? (Yes/No)')
        if start == 'Yes':
            Login_Interface_Python_Logic.login_interface()
            print("Let's start learning")
            learn_words()
        elif start == 'No':
            print('See you next time.')

if __name__ == '__main__':
    run()