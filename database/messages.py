from datetime import datetime

from database.connection import get_db_connection


def get_messaged_users(user_id):
    """
    Retrieves a list of users that the current user has exchanged messages with
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id, u.display_name, u.location, DATE(MAX(m.timestamp)) AS last_message_date
                                FROM user_data AS u
                                JOIN messages AS m
                                  ON u.user_id = m.from_user_id OR u.user_id = m.to_user_id
                               WHERE (m.from_user_id = %s OR m.to_user_id = %s)
                                 AND u.user_id != %s
                            GROUP BY u.user_id
                            ORDER BY MAX(m.timestamp) DESC""", [user_id, user_id, user_id])
            messages = cursor.fetchall()
            return messages


def get_messages_between_users(user_id_1, user_id_2):
    """
    Retrieves the messages between two users
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT m.from_user_id, m.to_user_id, m.timestamp, m.content
                                FROM messages AS m
                               WHERE (m.from_user_id = %s AND m.to_user_id = %s)
                                  OR (m.from_user_id = %s AND m.to_user_id = %s)
                            ORDER BY m.timestamp DESC""", [user_id_1, user_id_2, user_id_2, user_id_1])
            messages = cursor.fetchall()
            return messages


def add_message(from_user_id, to_user_id, content):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT INTO messages
                                          (from_user_id, to_user_id, timestamp, content)
                                   VALUES (%s, %s, %s, %s)""", [from_user_id, to_user_id, datetime.now(), content])
            connection.commit()
