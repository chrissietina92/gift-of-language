import mysql.connector
from config import USER, HOST, PASSWORD
from datetime import datetime, timedelta, date

# DB CONNECTION CREDENTIALS.
def _connect_to_db(db_name):
    connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
    return connection


def overalluserstreaksfunction(column, value):

# PART 1:
# CHECKING LAST DATE OF USER LOGIN.
# PYTHON QUERIES THE DB TO CHECK THE LAST DAY OF LOGIN.

    db_connection = None

    try:
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        print("Database connection Successful")


        #QUERY MADE TO MYSQL
        streaks_query_1 = "SELECT DATE_FORMAT(Lastlogin, '%d-%m-%Y') FROM the_users WHERE {COLUMN} = '{VALUE}';".format(
            COLUMN=column, VALUE=value)
        cur.execute(streaks_query_1)
        lastlogindata = cur.fetchall()
        cur.close()

        #FOR LOOP TO EXTRACT THE DATA FROM TUPLE CASING.
        for data in lastlogindata:
            lastlogin = data[0]


#PART 2 {IF STATEMENT AND 'NEW-USER-STREAK' FUNCTION}:
#INITIATES A LOGIN DATE AND USER STREAK AS 1, FOR NEW USERS.
#THIS CLAUSE IS A CONTINGENCY FOR USERS WHO ARE LOGGING IN FOR THE FIRST TIME.


        if lastlogin == None:

            lastlogindtobj = datetime.now().date()
            lastlogin = lastlogindtobj.strftime("%d-%m-%Y")

            # THE FUNCTION BELOW SETS THE NEW USERS STREAK TO 1.
            newuserstreak(column, value)
        else:
            print('We have your last login date')

        print("The last date of login was {}".format(str(lastlogin)))
        # return lastlogin

    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")


#PART 3:
# THIS FUNCTION USES THE LAST LOGIN DATE, TO CALCULATE THE TIME DIFFERENCE BETWEEN THE
# EXTRACTED DATE AND CURRENT DATE.
    calculatinglogindifference(lastlogin)

#PART 4 {ADJUST THE USER STREAK FUNCTION}:
# THE FUNCTION CALL IS NESTED TOWARDS THE END OF THE 'CALCULATING-LOGIN-DIFFRENCE' FUNCTION (SEE ABOVE).
# THE FUNCTION UPDATES THE USERSTREAKS IN THE DB.

#PART 5:
# THIS CONNECTS THE RESULTS OF THE DB UPDATE TO THE USER INTERFACE.
# THUS ALLOWING THE USER TO INCREASE ENGAGEMENT WITH THE APP.
    display_user_streak(column,value)



"""-------------------------------------------END OF OVERALL STREAKS CODE -------------------------------------------------"""


#PYTHON LOGIC BELOW REFERENCE THE ABOVE FUNCTIONS;

# REFERENCES PART 2:
def newuserstreak(column, value):

    db_connection = None

    try:
        # DB ENGINE.
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        print("Database connection Successful")


        #THIS QUERY SETS THE USER STREAK TO 1 IF THE USERS STREAK IS NONE (I.E. A NEW USER).
        new_streaker_update = "UPDATE the_users SET UserStreak = 1 WHERE {COLUMN} = '{VALUE}'".format(
            COLUMN=column, VALUE=value)
        cur.execute(new_streaker_update)
        db_connection.commit()
        cur.close()

    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")


#REFERENCES PART 3 ABOVE.
def calculatinglogindifference(lastlogin):

    # USING AND CONVERTING THE EXTRACTED LASTLOGIN DATE TO A DATETIME OBJECT.
    d1 = datetime.now().date()
    d2 = datetime.strptime(lastlogin, "%d-%m-%Y").date()

    # TESTING TO ENSURE THE FORMAT IS THE SAME; CAN BE DELETED.
    print("Today's date: {}".format(d1))
    print("Date of last login: {}".format(d2))

    # FINDING THE TIME DIFFERENCE BETWEEN THE FORMATTED DATES.
    # DELTA WILL OUTPUT THE DIFFERENCE IN DAYS.
    delta = d1 - d2
    login_difference = delta.days

    # TESTING TO ENSURE THE VARIABLE WORKS; CAN BE DELETED.
    print("Days since last login: {}".format(login_difference))
    # return login_difference

    # THIS FUNCTION USES THE LAST LOGIN DATE AND TIME DIFFERENCE PREVIOUSLY CALCULATED
    # TO UPDATE THE GOL USERS DB. A STREAK IS INCREASED OR RESET, DEPENDING ON THE CALCULATED TIME DIFFERENCE.
    adjusttheuserstreak(column, value, login_difference)


# REFERENCES PART 4 ABOVE
def adjusttheuserstreak(column, value, login_difference):

    #NOTE:
    #THE FOLLOWING CODE EXTRACTS THE DAYS DATE AND ASSIGNS IT TO THE VARIABLE AS A STR.
    #THIS ENABLES THE INFORMATION TO BE SENT INTO THE DB WITHOUT THROWING AN ERROR WITH MYSQL SYNTAX.
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    #A CHECK TO ENSURE THAT THE VARIABLE IS WORKING; CAN BE DELETED.
    print(type(today))
    print("TODAY: {}".format(today))


    db_connection = None

    try:
        # DB ENGINE.
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        print("Database connection Successful")


        #USES THE CALCULATED LOGIN DIFFERENCE TO ADJUST THE DB USER STREAK INFORMATION (ADDING ONE, STREAK RESET, PASS OVER WHERE APPLICABLE).
        if login_difference == 1:
            print("Thanks for joining today! Your streak goes up!")

            streaks_query_1 = "UPDATE the_users SET UserStreak = UserStreak + 1, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                COLUMN=column, VALUE=value, DATE=str(today))


        elif login_difference < 1:
            print("Keep up the hard work. \nDont forget to join us tomorrow too!")

            streaks_query_1 = "UPDATE the_users SET LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                COLUMN=column, VALUE=value, DATE=str(today))

        else:
            print("Nice to see you! It's been a long time.")
            streaks_query_1 = " UPDATE the_users SET UserStreak = 1, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                COLUMN=column, VALUE=value, DATE=today)

        cur.execute(streaks_query_1)
        db_connection.commit()
        cur.close()

    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")


# REFERENCES PART 5 ABOVE.
# THIS CALLS THE UPDATED USER STREAK FROM THE DB TO THE INTERFACE, ALLOWING THE USER TO ENGAGE WITH THE PROGRAM.

def display_user_streak(column, value):

    db_connection = None

    try:
        # DB ENGINE
        db_name = 'GOL_users'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()
        print("Database connection Successful")


        #THE QUERY CALLS THE USER STREAK NUMBER FROM THE DB, SO THAT IT CAN BE DISPLAYED ON THE INTERFACE.
        streaks_query_2 = "SELECT UserStreak FROM the_users WHERE {COLUMN} = '{VALUE}';".format(
            COLUMN=column, VALUE=value)

        cur.execute(streaks_query_2)
        streaks_result = cur.fetchall()

        # FOR LOOP TO EXTRACT DATE FROM TUPLE CASE.
        for days in streaks_result:
            streakvalue = days[0]

        print("Gift of Learning Streak: {} Days.".format(streakvalue))

    except Exception:
        raise ConnectionError

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")



# TESTING 1:
# WHERE LOGIN DATE VALUES ALREADY EXIST
# column = 'Username'
# value = 'cobrien1'
# overalluserstreaksfunction(column, value)


# TESTING 2:
# WHERE LAST LOGIN DATE WAS TODAY (FIRST TIME)
# column = 'Username'
# value = 'lucosov89'
# overalluserstreaksfunction(column, value)

# TESTING 3:
# WHERE LOGIN DATE VALUES DO NOT EXIST (FIRST TIME)
# column = 'Username'
# value = 'hbieber1997'
# overalluserstreaksfunction(column, value)
