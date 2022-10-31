import mysql.connector
from config import USER, HOST, PASSWORD
from datetime import datetime, timedelta, date

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

class TheUserStreak:

    def __init__(self, user_id_value, column, value):
        self.column = column
        self.value = value
        self.user_id = user_id_value
        self.last_login = None
        self.login_difference = None
        self.existing_user_streak = None

    def get_last_login(self):
        db_connection = None
        try:
            # DB ENGINE
            db_name = 'GOL_users'
            # Database engine
            db_connection = _connect_to_db(db_name)
            # Cursor
            cur = db_connection.cursor()

            # QUERY MADE TO MYSQL
            login_query = "SELECT DATE_FORMAT(Lastlogin, '%Y-%m-%d') FROM the_users WHERE {COLUMN} = '{VALUE}';".format(COLUMN=self.column, VALUE=self.value)

            cur.execute(login_query)
            lastlogindata = cur.fetchall()
            cur.close()
            # FOR LOOP TO EXTRACT THE DATA FROM TUPLE CASING.
            for data in lastlogindata:
                self.last_login = data[0]

            # THIS CLAUSE IS A CONTINGENCY FOR USERS WHO ARE LOGGING IN FOR THE FIRST TIME.
            if self.last_login is None:
                lastlogindtobj = datetime.now().date()
                self.last_login = lastlogindtobj.strftime("%Y-%m-%d")
                return False
            else:
                return True

        except Exception:
            raise ConnectionError

        finally:
            if db_connection:
                db_connection.close()



    def get_existing_user_streak(self):
        db_connection = None
        try:
            # DB ENGINE
            db_name = 'GOL_users'
            # Database engine
            db_connection = _connect_to_db(db_name)
            # Cursor
            cur = db_connection.cursor()

            streaks_query_01 = "SELECT " \
                               "UserStreak " \
                               "FROM " \
                               "the_users " \
                               "WHERE {COLUMN} = '{VALUE}';".format(COLUMN=self.column, VALUE=self.value)

            cur.execute(streaks_query_01)
            streaks_result = cur.fetchall()

            for days in streaks_result:
                self.existing_user_streak = days[0]

            if self.existing_user_streak == None:
                self.existing_user_streak = 1
                new_streaker = True
            else:
                new_streaker = False

            return new_streaker

        except Exception:
            raise ConnectionError

        finally:
            if db_connection:
                db_connection.close()


    def calculate_login_diff(self):
        # USING AND CONVERTING THE EXTRACTED LASTLOGIN DATE TO A DATETIME OBJECT.
        d1 = datetime.now().date()
        d2 = datetime.strptime(self.last_login, "%Y-%m-%d").date()

        # FINDING THE TIME DIFFERENCE BETWEEN THE FORMATTED DATES.
        # DELTA WILL OUTPUT THE DIFFERENCE IN DAYS.
        delta = d1 - d2
        self.login_difference = delta.days

        return "Days since last login: {}".format(self.login_difference)



    def update_userstreak_and_last_login(self):
        db_connection = None

        try:

            # NOTE:
            #     #THE FOLLOWING CODE EXTRACTS THE DAYS DATE AND ASSIGNS IT TO THE VARIABLE AS A STR.
            #     #THIS ENABLES THE INFORMATION TO BE SENT INTO THE DB WITHOUT THROWING AN ERROR WITH MYSQL SYNTAX.
            now = datetime.now()
            self.last_login = now.strftime("%Y-%m-%d")

            print("TODAY: {}".format(now.strftime("%d-%m-%Y")))

            # DB ENGINE
            db_name = 'GOL_users'
            # Database engine
            db_connection = _connect_to_db(db_name)
            # Cursor
            cur = db_connection.cursor()

            if self.login_difference == 1:
                print("Thanks for joining today! Your streak goes up!")
                streaks_query_02 = "UPDATE the_users SET UserStreak = UserStreak + 1, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                    COLUMN=self.column, VALUE=self.value, DATE=self.last_login)
                return "There has been a streak increase"

            elif self.login_difference < 1:
                print("Keep up the hard work. \nDont forget to join us tomorrow too!")
                streaks_query_02 = "UPDATE the_users SET UserStreak = {STREAK}, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                    COLUMN=self.column, VALUE=self.value, DATE=self.last_login, STREAK=self.existing_user_streak)
                return "The streak has stayed the same"
            else:
                print("Nice to see you! It's been a long time.")
                streaks_query_02 = " UPDATE the_users SET UserStreak = 1, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                    COLUMN=self.column, VALUE=self.value, DATE=self.last_login)
                return "The streak has been reset"

            cur.execute(streaks_query_02)
            db_connection.commit()
            cur.close()

            update_statement = 'System update complete.'
            return update_statement
        except Exception:
            raise ConnectionError

        finally:
            if db_connection:
                db_connection.close()


    def display_user_streak(self):
        db_connection = None

        try:
            # DB ENGINE
            db_name = 'GOL_users'
            # Database engine
            db_connection = _connect_to_db(db_name)
            # Cursor
            cur = db_connection.cursor()

            # THE QUERY CALLS THE USER STREAK NUMBER FROM THE DB, SO THAT IT CAN BE DISPLAYED ON THE INTERFACE.
            streaks_query_03 = "SELECT UserStreak FROM the_users WHERE {COLUMN} = '{VALUE}';".format(
                COLUMN=self.column, VALUE=self.value)

            cur.execute(streaks_query_03)
            streaks_result = cur.fetchall()

            # FOR LOOP TO EXTRACT DATE FROM TUPLE CASE.
            for days in streaks_result:
                final_streak = days[0]

            print("Gift of Learning Streak: {} Days.".format(final_streak))

            self.existing_user_streak = final_streak
            return self.existing_user_streak

        except Exception:
            raise ConnectionError

        finally:
            if db_connection:
                db_connection.close()


# TESTING
# test_01 = TheUserStreak(1, 'Username', 'cobrien1')
# print(test_01.get_last_login())
# print(test_01.get_existing_user_streak())
# print(test_01.calculate_login_diff())
# print(test_01.update_userstreak_and_last_login())
# print(test_01.display_user_streak())

test_02 = TheUserStreak(3, 'Username', 'hbieber1997')
test_02.get_last_login()
test_02.get_existing_user_streak()
test_02.calculate_login_diff()
test_02.update_userstreak_and_last_login()
test_02.display_user_streak()
#
# test_03 = TheUserStreak(4, 'Username', 'lucosov89')
# test_03.get_last_login()
# test_03.get_existing_user_streak()
# test_03.calculate_login_diff()
# test_03.update_userstreak_and_last_login()
# test_03.display_user_streak()


