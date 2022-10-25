import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        database='motivational_quotes',
        host='localhost',
        user='admin',
        password='admin'
    )

def get_random_quote():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT * FROM inspirational_quotes ORDER BY rand() LIMIT 1""")
            result = cursor.fetchone()
    return result['quotes']


if __name__ == '__main__':
    print(get_random_quote())
