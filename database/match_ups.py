from database.connection import get_db_connection


def get_match(current_user_id, exclude):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id, u.display_name, u.about, u.location
                                FROM user_data AS u
                                WHERE u.user_id NOT IN (SELECT u.user_id
                                                          FROM user_data AS u
                                                          JOIN messages AS m
                                                            ON u.user_id = m.from_user_id OR u.user_id = m.to_user_id
                                                         WHERE (m.from_user_id = %s OR m.to_user_id = %s)
                                                           AND u.user_id != %s
                                                      GROUP BY u.user_id)
                                AND u.user_id NOT IN (%s, %s)
                                ORDER BY rand() LIMIT 1""", [current_user_id, current_user_id, current_user_id, current_user_id, exclude])
            result = cursor.fetchone()
            return result
