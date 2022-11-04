from database.connection import get_db_connection


def get_random_quote():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, quote
                                FROM inspirational_quotes
                                ORDER BY rand()
                                LIMIT 1""")
            result = cursor.fetchone()
            return result
