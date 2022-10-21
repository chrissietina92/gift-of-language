import mysql.connector
from config import USER, PASSWORD, HOST


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


def show_word_and_definition(result):
    for word in result:
        print('The word is: {}'.format(word))
        print('The definition is: {}'.format(result[word]))


# EXAMPLE 1
def get_word_learnt(word):
    try:
        db_name = 'dictionary'
        #Database Engine
        db_connection = _connect_to_db(db_name)
        #Cursor
        cur = db_connection.cursor()
        print("Database successfully connected")

        query = "SELECT word, definition_ FROM learnt_words WHERE word = '{}'".format(word)

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        result = dict(result)

        word_learnt = show_word_and_definition(result)
    except:
        raise DbConnectionError
    finally:
        if db_connection:
            db_connection.close()
            print("DBConnection closed")
    return word_learnt

def add_new_word(new_word, definition):
    try:
        db_name = 'dictionary'
        #Database Engine
        db_connection = _connect_to_db(db_name)
        #Cursor
        cur = db_connection.cursor()
        print("Database successfully connected")

        query = "INSERT INTO learnt_words(word, definition_) VALUES ('{}', '{}');".format(new_word, definition)
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except:
        raise DbConnectionError
    finally:
        if db_connection:
            db_connection.close()
            print("DBConnection closed")



if __name__ == '__main__':
    pass
