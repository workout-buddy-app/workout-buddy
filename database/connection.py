import mysql.connector
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS




def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
    )