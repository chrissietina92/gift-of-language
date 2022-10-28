import mysql.connector
from config import USER, HOST, PASSWORD

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



def does_user_exist(column, value):
    db_connection = None
    try:
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        # print("Database connection Successful")

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

        cur.close()
    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection closed")


def add_a_new_user(userid, firstname, lastname, email, dob, city, username, password):
    db_connection = None
    try:
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        # print("Database connection Successful")

        query = """
                INSERT INTO the_users (UserID, FirstName, LastName, Email, DOB, City, Username, UserPassword)
                VALUES ('{USERID}', '{FIRSTNAME}', '{LASTNAME}', '{EMAIL}', str_to_date('{DOB}', '%d-%m-%Y'), '{CITY}', '{USERNAME}', '{PASSWORD}')
                """.format(USERID=userid, FIRSTNAME=firstname, LASTNAME=lastname, EMAIL=email, DOB=dob,
                           CITY=city, USERNAME=username, PASSWORD=password)
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            #print("DB connection closed")


def new_user_credentials():
    # This function implements the add_a_new_user function.
    # The function was created to prevent the repeat of code.

    email = input('Email: ')
    userid = input('User id: ')
    firstname = input('First name: ')
    lastname = input('Last name: ')
    dob = input('DOB (%d-%m-%Y): ')
    city = input('City: ')
    username = input('Username: ')
    password = input('Password: ')
    add_a_new_user(userid, firstname, lastname, email, dob, city, username, password)



def username_and_password_match(column, value, password_value):
    db_connection = None
    try:

        user_attempt = 0
        while user_attempt < 2:

            db_name = 'GOL_users'
            # Database engine
            db_connection = _connect_to_db(db_name)
            # Cursor
            cur = db_connection.cursor()
            #print("Database connection Successful")

            # This query checks if the records of the password and username exist in one record. It returns 1 if it does exist and 0 if it does not exist.
            query = "SELECT(EXISTS(SELECT FirstName FROM the_users WHERE {} = '{}' AND UserPassword = '{}'))".format(column,value,password_value)

            cur.execute(query)
            result2 = cur.fetchall()


            if result2[0][0] == 1:
                # This query calls the users first name, if the login has been successful.
                query2 = "SELECT FirstName FROM the_users WHERE {} = '{}' AND UserPassword = '{}'".format(
                    column, value, password_value)
                cur.execute(query2)
                result3 = cur.fetchall()

                # This for loop extracts the first name from the tuple case.
                for data in result3:
                    name = data[0]

                print("Login Successful. \nWelcome, {}".format(name))
                return True
                break

            else:
                # return False  # will be needed, this section may have to be removed as not sure how it will work with front end
                user_attempt += 1
                print('Incorrect credentials. Please try again')
                password_value = input("Enter your password.")

        else:
            print("You have entered an incorrect password several times; you are now locked out of your account.\nPlease contact your customer care for support.")
            return False
        cur.close()

    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            #print("DB connection closed")



