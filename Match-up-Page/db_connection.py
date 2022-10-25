from mysql.connector import connect

# from config import DB_HOST, DB_USER, DB_PASS, DB_NAME


def get_db_connection():
    connection = connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME)
    return connection


DB_NAME = 'workout-buddies-dummy'
DB_HOST = 'localhost'
DB_USER = 'admin'     # Change this value according to your own setup
DB_PASS = 'admin'               # Change this value according to your own setup

FLASK_SECRET = 'flask_secret'   # Generate a random string to use for your Flask secret key
FLASK_DEBUG = True
