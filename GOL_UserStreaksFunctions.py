import mysql.connector
from config import USER, HOST, PASSWORD
from datetime import datetime, timedelta, date
from GOL_DB_Connection_Decorator import _connect_to_db, db_connection_decorator

db_name = 'GOL_users'
db_connection = None


class TheUserStreak:

    def __init__(self, column, value, last_login=None, login_difference=None, existing_user_streak=1):
        self.column = column
        self.value = value
        self.last_login = last_login
        self.login_difference = login_difference
        self.existing_user_streak = existing_user_streak

    @db_connection_decorator
    def get_last_login(self, cur, db_connection):
        # QUERY MADE TO MYSQL
        login_query = "SELECT DATE_FORMAT(Lastlogin, '%Y-%m-%d') FROM the_users WHERE {COLUMN} = '{VALUE}';".format(
            COLUMN=self.column, VALUE=self.value)

        cur.execute(login_query)
        lastlogindata = cur.fetchall()

        # FOR LOOP TO EXTRACT THE DATA FROM TUPLE CASING.
        for data in lastlogindata:
            self.last_login = data[0]

        # THIS CLAUSE IS A CONTINGENCY FOR USERS WHO ARE LOGGING IN FOR THE FIRST TIME.
        if self.last_login is None:
            lastlogindtobj = datetime.now().date()
            self.last_login = lastlogindtobj.strftime("%Y-%m-%d")
            return self.last_login
        else:
            return self.last_login

    @db_connection_decorator
    def get_existing_user_streak(self, cur, db_connection):
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
        return self.existing_user_streak

    def calculate_login_diff(self):
        # USING AND CONVERTING THE EXTRACTED LASTLOGIN DATE TO A DATETIME OBJECT.
        d1 = datetime.now().date()
        d2 = datetime.strptime(self.last_login, "%Y-%m-%d").date()

        # FINDING THE TIME DIFFERENCE BETWEEN THE FORMATTED DATES.
        # DELTA WILL OUTPUT THE DIFFERENCE IN DAYS.
        delta = d1 - d2
        self.login_difference = delta.days

        if self.login_difference < 0 or self.login_difference is None:
            raise ValueError("System error. Unable to calculate time since last logged in. Please try again later.")
        else:
            return "Days since last login: {}".format(self.login_difference)

    @db_connection_decorator
    def update_userstreak_and_last_login(self, cur, db_connection):
        # NOTE:
        #     #THE FOLLOWING CODE EXTRACTS THE DAYS DATE AND ASSIGNS IT TO THE VARIABLE AS A STR.
        #     #THIS ENABLES THE INFORMATION TO BE SENT INTO THE DB WITHOUT THROWING AN ERROR WITH MYSQL SYNTAX.
        now = datetime.now()
        self.last_login = now.strftime("%Y-%m-%d")

        if self.login_difference == 1:
            streaks_query_02 = "UPDATE the_users SET UserStreak = UserStreak + 1, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                COLUMN=self.column, VALUE=self.value, DATE=self.last_login)
            closing_message = "Thanks for joining today! Your streak goes up!"

        elif self.login_difference == 0:
            streaks_query_02 = "UPDATE the_users SET LastLogin = '{DATE}', UserStreak = '{US}', LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                COLUMN=self.column, VALUE=self.value, DATE=self.last_login, US=self.existing_user_streak)
            closing_message = "Keep up the hard work. \nDont forget to join us tomorrow too!"

        elif self.login_difference > 1:
            streaks_query_02 = " UPDATE the_users SET UserStreak = 1, LastLogin = '{DATE}' WHERE {COLUMN} = '{VALUE}'".format(
                COLUMN=self.column, VALUE=self.value, DATE=self.last_login)
            closing_message = "Nice to see you! It's been a long time."

        else:
            raise ValueError

        cur.execute(streaks_query_02)
        db_connection.commit()
        return print(closing_message)

    @db_connection_decorator
    def display_user_streak(self, cur, db_connection):
        # THE QUERY CALLS THE USER STREAK NUMBER FROM THE DB, SO THAT IT CAN BE DISPLAYED ON THE INTERFACE.
        streaks_query_03 = "SELECT UserStreak FROM the_users WHERE {COLUMN} = '{VALUE}';".format(
            COLUMN=self.column, VALUE=self.value)

        cur.execute(streaks_query_03)
        streaks_result = cur.fetchall()

        # FOR LOOP TO EXTRACT DATE FROM TUPLE CASE.
        for days in streaks_result:
            final_streak = days[0]

        self.existing_user_streak = final_streak
        return print("Gift of Learning Streak: {} Day(s).".format(self.existing_user_streak))


# TESTING

def runTheUsersFunction(column, value):
    the_user = TheUserStreak(column, value)
    the_user.get_last_login()
    the_user.get_existing_user_streak()
    the_user.calculate_login_diff()
    the_user.update_userstreak_and_last_login()
    the_user.display_user_streak()


# TESTING
# column = "Username"
# value = "freddy95"
# runTheUsersFunction(column, value)

