import itertools
import os
from src.db_functions import db_connection_decorator
from src.dictionaryapi_functions import get_definition



#import connection from db_function
class DbConnectionError(Exception):
    pass

@db_connection_decorator
def check_if_word_in_database_for_user(word, userid, cur, db_connection):
    query = "SELECT word FROM searched_words WHERE UserID = {};".format(userid)
    cur.execute(query)
    result = cur.fetchall()
    result = [list(i) for i in result]
    final_result = list(itertools.chain(*result))
    if word.lower() in final_result:
        return True
    else:
        return False


@db_connection_decorator
def add_searched_word(new_word, userid, cur, db_connection):
    if not check_if_word_in_database_for_user(new_word, userid):
        definition = get_definition(new_word)
        # with open('../docs/SearchedWords.txt', 'a') as file: file.write("{} - {} \n".format(new_word.lower(), definition)) #no longer using
        query = 'INSERT INTO searched_words(UserID, word, definition_) VALUES ("{}", "{}", "{}");'.format(userid, new_word.lower(), definition)
        cur.execute(query)
        db_connection.commit()

@db_connection_decorator
def display_users_searched_word(userid, cur, db_connection):
    query = """SELECT word, definition_
                FROM searched_words
                WHERE UserID = {} ;""".format(userid)
    cur.execute(query)
    result = cur.fetchall() # a list of tuples
    return result


# print(display_users_searched_word(1))


## THESE 3 FUNCTIONS BELOW AREN'T USED ANYMORE
# @db_connection_decorator
# def clean_db_for_new_user(cur, db_connection):
#     query = 'TRUNCATE TABLE searched_words;'
#     cur.execute(query)
#     db_connection.commit()
#
#
# def display_all_searched_words():
#      try:
#          file= open("../docs/SearchedWords.txt", "r")
#      except FileNotFoundError:
#          print("You haven't searched any words yet.")
#      else:
#          print(file.read())
#          file.close()
# #
# def delete_searched_words():
#     try:
#         file = open("../docs/SearchedWords.txt", "r")
#     except FileNotFoundError:
#         return
#     else:
#         file.close()
#         os.remove('../docs/SearchedWords.txt')

