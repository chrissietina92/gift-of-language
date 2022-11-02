import mysql.connector
from config import USER, HOST, PASSWORD

# THE DECORATOR

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

def db_connection_decorator(func):
    def wrapper(*args):
        db_connection = None
        try:
            db_name = 'GOL_users'
            db_connection = _connect_to_db(db_name)
            # print("Connection successful")
            cur = db_connection.cursor()
            result = func(*args, cur, db_connection)
            return result
            cur.close()
        except Exception:
            raise ConnectionError

        finally:
            if db_connection:
                db_connection.close()
                # print("DB connection closed")
    return wrapper