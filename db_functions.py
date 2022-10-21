import mysql.connector
from config import USER, HOST, PASSWORD

class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
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
        print("Database connection Successful")

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
            print('A user exists with these details')
        else:
            print('A user does not exist with these details')

        cur.close()
    except Exception:
        raise DbConnectionError

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")


def add_a_new_user(userid, firstname, lastname, email, dob, city, username, password):
    db_connection = None
    try:
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        print("Database connection Successful")

        query = """
                INSERT INTO the_users (UserID, FirstName, LastName, Email, DOB, City, Username, UserPassword)
                VALUES ('{USERID}', '{FIRSTNAME}', '{LASTNAME}', '{EMAIL}', str_to_date('{DOB}', '%d-%m-%Y'), '{CITY}', '{USERNAME}', '{PASSWORD}')
                """.format(USERID=userid, FIRSTNAME=firstname, LASTNAME=lastname, EMAIL=email, DOB=dob,
                           CITY=city, USERNAME=username, PASSWORD=password)
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")


