import mysql.connector
import itertools
import os
from db_functions import db_connection_decorator, _connect_to_db
from config import USER, PASSWORD, HOST
from src.api import get_definition



#import connection from db_function
class DbConnectionError(Exception):
    pass

@db_connection_decorator
def check_if_word_in_database(word, cur, db_connection):
    query = "SELECT word FROM searched_words; "
    cur.execute(query)
    result = cur.fetchall()
    result = [list(i) for i in result]
    final_result = list(itertools.chain(*result))
    if word.lower() in final_result:
        return True
    else:
        return False


@db_connection_decorator
def add_searched_word(new_word, cur, db_connection):
    if not check_if_word_in_database(new_word):
        definition = get_definition(new_word)
        with open('../docs/SearchedWords.txt', 'a') as file: file.write("{} - {} \n".format(new_word.lower(), definition))
        query = "INSERT INTO searched_words(word, definition_) VALUES ('{}', '{}');".format(new_word.lower(), definition)
        cur.execute(query)
        db_connection.commit()

# add_searched_word('cat')

## THESE 2 FUNCTIONS BELOW NEED TO BE PUT IN A SEPERATE FILE
@db_connection_decorator
def clean_db_for_new_user(cur, db_connection):
    query = 'TRUNCATE TABLE searched_words;'
    cur.execute(query)
    db_connection.commit()

clean_db_for_new_user()

def display_all_searched_words():
    try:
        file= open("../docs/SearchedWords.txt", "r")
    except FileNotFoundError:
        print("You haven't searched any words yet.")
    else:
        print(file.read())
        file.close()

def delete_searched_words():
    try:
        file = open("../docs/SearchedWords.txt", "r")
    except FileNotFoundError:
        return
    else:
        file.close()
        os.remove('../docs/SearchedWords.txt')