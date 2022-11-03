import itertools
import os
from db_functions import db_connection_decorator
from dictionary_api_functions import get_definition



# Import connection from db_function
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