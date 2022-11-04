import bcrypt
from database.connection import get_db_connection


def add_user(name, email, password, date_birth):
    """
    Adds a new user to the database.
    Raises an error if the email already exists in the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            cursor.execute("""INSERT
                                INTO user_login
                                     (name, email, hashed_password, date_birth)
                                 VALUES (%s, %s, %s, %s);""", [name, email, hashed_password, date_birth])

            connection.commit()


def email_available(email):
    """
    Checks whether an email is available or whether it is already present in the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id, u.name, u.email, u.date_birth
                                FROM user_login AS u
                               WHERE u.email = %s""", [email])
            matching_user = cursor.fetchone()
            return True if matching_user is None else False


def get_user_with_credentials(email, password):
    """
    Retrieves the user with the given credentials, if present.
    If there is no matching user, returns None.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            cursor.execute("""SELECT u.user_id, u.name, u.email, u.hashed_password, u.date_birth
                                FROM user_login AS u
                               WHERE u.email = %s""", [email])

            matching_user = cursor.fetchone()
            if matching_user is not None and bcrypt.checkpw(password_bytes, matching_user.get('hashed_password')):
                return matching_user


def get_user_by_id(user_id):
    """
    Retrieves the user with the given id, if present.
    If there is no matching user, returns None.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id, u.name, u.email
                                FROM user_login AS u
                               WHERE u.user_id = %s""", [user_id])

            matching_user = cursor.fetchone()
            return matching_user


def get_public_profile_data(user_id):
    """
    Retrieves the public profile data for the user with the given id, if present.
    If there is no matching user, returns None.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id, u.display_name, u.about, u.location
                                FROM user_data AS u
                               WHERE u.user_id = %s""", [user_id])

            matching_user = cursor.fetchone()
            return matching_user


def update_public_profile(user_id, display_name, about, location):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""UPDATE user_data
                                 SET display_name = %s, 
                                     about = %s,
                                     location = %s
                               WHERE user_id = %s""", [display_name, about, location, user_id])
            connection.commit()
