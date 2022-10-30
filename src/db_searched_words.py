import mysql.connector
import itertools
import os
from src.db_functions import db_connection_decorator, _connect_to_db, new_user
from config import USER, PASSWORD, HOST
from src.api import get_definition


class user_db:
    def __init__(self):
        self.user = new_user()

    # import connection from db_function
    class DbConnectionError(Exception):
        pass

    @db_connection_decorator
    def check_if_word_in_database(self,word, cur, db_connection):
        query = "SELECT word FROM searched_words_user_{}; ".format(self.user.userid)
        cur.execute(query)
        result = cur.fetchall()
        result = [list(i) for i in result]
        final_result = list(itertools.chain(*result))
        if word.lower() in final_result:
            return True
        else:
            return False

    @db_connection_decorator
    def add_searched_word(self, new_word, cur, db_connection):
        if not self.check_if_word_in_database(new_word) and get_definition(new_word)!='This word does not exist in the dictionary.':
            definition = get_definition(new_word)
            with open('SearchedWords_{}.txt'.format(self.user.userid), 'a') as file: file.write("{} - {} \n".format(new_word.lower(), definition))
            query = "INSERT INTO searched_words_user_{}(word, definition_) VALUES ('{}', '{}');".format(self.user.userid, new_word.lower(), definition)
            cur.execute(query)
            db_connection.commit()

    # add_searched_word('cat')


    @db_connection_decorator
    def create_db_for_new_user(self, cur, db_connection):
        self.user.new_user_credentials()
        query = 'CREATE TABLE searched_words_user_{}(word varchar(50) NOT NULL, definition_ varchar(6000) NOT NULL);'.format(self.user.userid)
        cur.execute(query)
        db_connection.commit()

    def display_all_searched_words(self):
        try:
            file = open("SearchedWords_{}.txt".format(self.user.userid), "r")
        except FileNotFoundError:
            print("You haven't searched any words yet.")
        else:
            print(file.read())
            file.close()

