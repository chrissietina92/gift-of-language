import mysql.connector
from config import USER, PASSWORD, HOST
from api import get_definition
import itertools
import os


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def check_if_word_in_database(word):
    try:
        db_name = 'GOL_users'
        #Database Engine
        db_connection = _connect_to_db(db_name)
        #Cursor
        cur = db_connection.cursor()

        query = "SELECT word FROM searched_words; "

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        result = [list(i) for i in result]
        final_result = list(itertools.chain(*result))
        if word in final_result:
            return True
        else:
            return False

    except:
        raise DbConnectionError
    finally:
        if db_connection:
            db_connection.close()

def display_all_searched_words():
    try:
        file= open("SearchedWords.txt", "r")
    except FileNotFoundError:
        print("You haven't searched any words yet.")
    else:
        print(file.read())
        file.close()

def add_searched_word(new_word):
    try:
        db_name = 'GOL_users'
        #Database Engine
        db_connection = _connect_to_db(db_name)
        #Cursor
        cur = db_connection.cursor()
        #print("Database successfully connected")

        if not check_if_word_in_database(new_word):
            definition = get_definition(new_word)
            with open('SearchedWords.txt', 'a') as file:
                file.write("{} - {} \n".format(new_word, definition))
            query = "INSERT INTO searched_words(word, definition_) VALUES ('{}', '{}');".format(new_word, definition)
            cur.execute(query)
            db_connection.commit()
            cur.close()
    except:
        raise DbConnectionError
    finally:
        if db_connection:
            db_connection.close()
            #print("DBConnection closed")

## THESE 2 FUNCTIONS BELOW NEED TO BE PUT IN A SEPERATE FILE
def clean_db_for_new_user():
    try:
        db_name = 'GOL_users'
        #Database Engine
        db_connection = _connect_to_db(db_name)
        #Cursor
        cur = db_connection.cursor()
        #print("Database successfully connected")

        query = 'TRUNCATE TABLE searched_words;'
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except:
        raise DbConnectionError
    finally:
        if db_connection:
            db_connection.close()
            #print("DBConnection closed")


def delete_searched_words():
    try:
        file = open("SearchedWords.txt", "r")
    except FileNotFoundError:
        return
    else:
        file.close()
        os.remove('SearchedWords.txt')