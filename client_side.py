from db_functions import does_user_exist, add_a_new_user

option = int(input("""Would you like to 
                    (1) check if a user exists
                    (2) add a new user
                    Choice (1/2): """ ))

if option == 1:
    column = input('How would you like to search for user? (FirstName/LastName/Email/Username)' )
    value = input('{}: '.format(column))
    does_user_exist(column, value)
else:
    userid = input('User id: ')
    firstname = input('First name: ')
    lastname = input('Last name: ')
    email = input('Email: ')
    dob = input('DOB (%d-%m-%Y): ')
    city = input('City: ')
    username = input('Username: ')
    password = input('Password: ')
    add_a_new_user(userid, firstname, lastname, email, dob, city, username, password)