from mysql.connector import connect

from config import DB_HOST, DB_USER, DB_PASS, DB_NAME


def get_db_connection():
    connection = connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME)
    return connection
