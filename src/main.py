from src.Login_Interface_Python_Logic import login_interface
from src.daily_words import randomWordGenerator
from src.db_searched_words import user_db
from src.api import show_word_and_definition
import schedule
import time
import re
from datetime import timedelta, datetime

class user_:
    def __init__(self):
        self.user = user_db()

    def set_reminder_time(self):
        reminderTime = input("Please enter the time you would like your daily reminder in 24hr format:")
        regex = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
        pat = re.compile(regex)
        # searching regex
        mat = re.search(pat, reminderTime)
        # validating conditions
        if mat:
            # Every day at 'reminderTime' time randomWordGenerator() is called.
            # now = datetime.now()
            # after_2_sec = now + timedelta(seconds=2)
            # after_2_sec = after_2_sec.time()
            # after_2_sec = f'{after_2_sec:%H:%M:%S}'
            schedule.every().day.at("{}".format(reminderTime)).do(randomWordGenerator)
            schedule.every().day.at("{}".format(reminderTime)).do(self.continue_learning)
            print("Your reminder has been set")
            # Loop so that the scheduling task
            # keeps on running all time.
            # learn_words()
            while True:
                # Checks whether a scheduled task
                # is pending to run or not
                schedule.run_pending()
                time.sleep(1)
        else:
            print('Please enter the right format of the time HH:MM')
            self.set_reminder_time()


    def learn_words(self):
        start = input(
            'Would you like to search your Schedule your words, Search your Dictionary, or View your Searched Words? (Schedule Word/Search Dictionary/View Searched Words) ').lower()
        if start == 'schedule word':
            self.set_reminder_time()
        elif start == 'search dictionary':
            self.search_words_in_dictionary()
            self.continue_learning()
        elif start == 'view searched words':
            self.user.display_all_searched_words()
            self.continue_learning()
        else:
            print('Please try again')
            self.continue_learning()

    def search_words_in_dictionary(self):
        search_again = input('Would you like to continue searching your dictionary? (Yes/No) ').lower()
        if search_again == 'no':
            print('You are leaving your dictionary...')
            return
        elif search_again == 'yes':
            search = input('Please search for a word in your dictionary: ')
            show_word_and_definition(search)
            self.user.add_searched_word(search)
            self.search_words_in_dictionary()
        else:
            print('Please try again.')
            self.search_words_in_dictionary()

    def continue_learning(self):
        cont_learning = input('Would you like to continue? (Yes/No) ').lower()
        if cont_learning == 'no':
            print('See you next time.')
            exit(0)
        elif cont_learning == 'yes':
            self.learn_words()
        else:
            print("Please type 'Yes' or 'No'")
            self.continue_learning()

    def run(self):
        print('##################################')
        print('Hello, welcome to the Gift of Language')
        print('##################################')
        print()
        self.run_user_input()

    def run_user_input(self):
        option = input("""Would you like to 
                                (1) Login as an existing user
                                (2) Register as a new user
                                Choice (1/2): """)
        if option == '1':
            if login_interface():
                print("Let's start learning")
                self.learn_words()

        elif option == '2':
            print('Please register adding the required information.')
            self.user.create_db_for_new_user()
            print("Congratulations! Registration completed.")
            start = input('Would you like to log in with your new account to start learning? (Yes/No)').lower()
            if start == 'yes':
                login_interface()
                print("Let's start learning")
                self.learn_words()
            elif start == 'no':
                print('See you next time.')
            else:
                print('Please try again.')
                self.learn_words()
        else:
            print('Please try again. Please select one of the two options.')
            self.run_user_input()


user = user_()
user.run()