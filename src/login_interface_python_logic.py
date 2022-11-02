from src.db_functions import _connect_to_db, does_user_exist, new_user_credentials, username_and_password_match
from db_functions import check_if_valid_username, get_user_by_column
# Welcome message.
#print("The Gift of Language")
#print("Welcome.")

# Programme query to customer.
# This function checks whether the customer has an existing account or not to their knowledge.
# If customer inputs that they do not, this gives them an opportunity to sign up for an account.

def existing_customer_check():
    existing_user_query = input("Do you have an existing account with us? (y/n)")
    user_existing_feedback = existing_user_query.lower()

    if user_existing_feedback == 'y':
        login_interface()
    elif user_existing_feedback == 'n':
        print("Create a new account.")
        new_user_credentials()
        # New user information input.
        # This is added to the DB via the add_a_new_user function called.
    else:
        raise TypeError("You have entered an invalid character.")


def login_interface():
    login_method = input('How would you like to login? (Email/Username)')
    column = login_method.title()
    matched = False
    userid = 0
    if column == 'Email' or column == 'Username':
        value = input('Enter your {}: '.format(column.lower()))
        print("Thank you. Checking your details...")
        if not check_if_valid_username(username=value):
            print("You haven't entered a valid username. Please try again.")
            login_interface()
        else:
            does_user_exist(column, value)
            password_value = input("Enter your password:")
            matched = username_and_password_match(column, value, password_value)
            userid = 0
            if matched:
                userid = get_user_by_column(column, value)

    else:
        print('Please try again, choosing one of the options.')
        login_interface()
    return matched, userid


_connect_to_db('GOL_users')




# For testing the code:
# password_input = 'helloworld0'
# username_and_password_match('Email', 'lucosovino89@email.com', password_input)
