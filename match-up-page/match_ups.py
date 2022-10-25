from db_management import get_db_connection


def get_info():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT *
                            FROM user_data""")
            users = cursor.fetchall()
            return users


print(get_info())


def get_match():
    # needs to select one profile, not the current user
    # cannot repeat matches in a session
    # should randomise
    # needs at least to get name/username, picture, and bio
    pass


def accept_match():
    # if choose this go to chat page
    # what about consent from the other person? or would it just ping them
    # print a warning message before redirection
    pass


def reject_match():
    # if choose this, cycle back into get_match
    pass


def quit_matching():
    # may not  need this as is webpage????
    # returns user to dashboard page or homepage
    pass


def user_interface():
    pass


def push_notification_to_accepted_match():
    pass

