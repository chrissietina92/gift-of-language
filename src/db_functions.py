import mysql.connector
from config import USER, HOST, PASSWORD
import re

#db_name = 'GOL_users'

# convert this into a decorator for other functions
def _connect_to_db(db_name):
    #attribute
    connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
    return connection

def db_connection_decorator(func):
    def wrapper(*args):
        db_connection = None
        try:
            db_name = 'GOL_users'
            db_connection = _connect_to_db(db_name)
            cur = db_connection.cursor()
            result = func(*args, cur, db_connection)
            return result
            cur.close()
        except Exception:
            raise ConnectionError

        finally:
            if db_connection:
                db_connection.close()
                # print("DB connection closed")
    return wrapper

@db_connection_decorator
def does_user_exist(column, value, cur, db_connection):
    query = """
            SELECT (EXISTS(SELECT FirstName
            FROM the_users
            WHERE {COLUMN} = '{VALUE}'));
            """.format(COLUMN = column, VALUE = value)
    cur.execute(query)
    result = cur.fetchall()
    # print(result)
    ## THE ABOVE QUEUERY WILL EITHER RETURN
    ## [(1,)] WHICH REPRESENTS TRUE
    ## OR [(0,)] WHICH REPRESENTS FALSE
    if result[0][0] == 1:
        return True
    else:
        return False



@db_connection_decorator
def add_a_new_user(firstname, lastname, email, dob, city, username, password, cur, db_connection):
    query = """
            INSERT INTO the_users (FirstName, LastName, Email, DOB, City, Username, UserPassword)
            VALUES ('{FIRSTNAME}', '{LASTNAME}', '{EMAIL}', str_to_date('{DOB}', '%d-%m-%Y'), '{CITY}', '{USERNAME}', '{PASSWORD}')
            """.format(FIRSTNAME=firstname, LASTNAME=lastname, EMAIL=email, DOB=dob,
                        CITY=city, USERNAME=username, PASSWORD=password)
    cur.execute(query)
    db_connection.commit()

@db_connection_decorator
def get_user_by_id(userid, cur, db_connection):
    query = """SELECT UserID, Firstname, Lastname, Username
                FROM the_users
                WHERE UserID = {USERID};""".format(USERID=userid)
    cur.execute(query)
    result = cur.fetchall()
    return result

@db_connection_decorator
def get_user_by_column(column, value, cur, db_connection):
    query = """SELECT UserID
                FROM the_users
                WHERE {COLUMN} = '{VALUE}';""".format(COLUMN=column, VALUE=value)
    cur.execute(query)
    result = cur.fetchall()
    userid = result[0][0]
    return userid

# print(get_user_by_column('Username', 'Fishy'))

@db_connection_decorator
def username_and_password_match(column, value, password_value, cur, db_connection):
    # This query checks if the records of the password and username exist in one record. It returns 1 if it does exist and 0 if it does not exist.
    query = "SELECT(EXISTS(SELECT FirstName FROM the_users WHERE {} = '{}' AND UserPassword = '{}'))".format(column,value,password_value)
    cur.execute(query)
    result2 = cur.fetchall()
    if result2[0][0] == 1:
        # This query calls the users first name, if the login has been successful.
        query2 = "SELECT FirstName FROM the_users WHERE {} = '{}' AND UserPassword = '{}'".format(column, value, password_value)
        cur.execute(query2)
        result3 = cur.fetchall()
        # This for loop extracts the first name from the tuple case.
        for data in result3:
            name = data[0]
            print("Login Successful. \nWelcome, {}".format(name))
        return True
    else:
        print("You have entered an incorrect password ; you are now locked out of your account.\nPlease contact your customer care for support.")
        return False


def new_user_credentials():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # This function implements the add_a_new_user function.
    # The function was created to prevent the repeat of code.
    username = input('Username -> Total length of the username should be between 4 and 20.\n'
                     'It should start with a letter.\n'
                     'Contains only letters, numbers, underscores and dashes.\n'
                     'Username: ')
    while not check_if_valid_username(username):
        print("You have entered an invalid username. Please try again")
        username = input('Username: ')
    email = input('Email: ')
    while not (re.fullmatch(regex, email)):
        print('You have entered an invalid email. Please try again.')
        email = input('Email: ')
    password = input('Password -> 1. Should have at least one number;\n'
                     ' 2. Should have at least one uppercase and one lowercase character.\n'
                     '3. Should have at least one special symbol.\n'
                     '4. Should be between 6 to 20 characters long: \n'
                     'Password: ')
    while not check_if_valid_password(password):
        print("Please enter e valid password")
        password = input('Password: ')
    firstname = input('First name: ')
    while not check_if_valid_name(firstname):
        print("Please enter e valid name")
        firstname = input('Name: ')
    lastname = input('Last name: ')
    while not check_if_valid_name(lastname):
        print("Please enter e valid last name")
        lastname = input('Name: ')
    dob = input('DOB (%d-%m-%Y): ')
    city = input('City: ')
    while not check_if_valid_name(city):
        print("Please enter e valid city")
        city = input('Name: ')
    if does_user_exist('Email', email) or does_user_exist('Username', username):
        duplicate = True
    else:
        duplicate = False
        add_a_new_user(firstname, lastname, email, dob, city, username, password)
    return duplicate


def check_if_valid_password(passwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    # compiling regex
    pattern = re.compile(reg)
    # searching regex
    match = re.search(pattern, passwd)

    # validating conditions
    if match:
        return True
    else:
        return False


def check_if_valid_username(username):
    reg = "^[A-Za-z0-9_-]{4,20}$"
    # compiling regex
    pattern = re.compile(reg)
    # searching regex
    match = re.search(pattern, username)

    # validating conditions
    if match:
        return True
    else:
        return False


def check_if_valid_name(name):
    reg = "^[A-Za-z]{2,25}$"
    # compiling regex
    pattern = re.compile(reg)
    # searching regex
    match = re.search(pattern, name)
    # validating conditions
    if match:
        return True
    else:
        return False


