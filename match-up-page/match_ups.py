from db_management import get_db_connection


# def get_info():
#     with get_db_connection() as connection:
#         with connection.cursor(dictionary=True) as cursor:
#             cursor.execute("""SELECT *
#                             FROM user_data""")
#             users = cursor.fetchall()
#             return users


# print(get_info())


def get_match():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT ud.display_name, ud.about, ud.location 
                                FROM user_data AS ud
                                ORDER BY rand() LIMIT 1""")
            result = cursor.fetchone()
    return result
    # needs to select one profile, not the current user ??
    # cannot repeat matches in a session
    # should randomise XX
    # needs at least to get name/username, picture, and bio XX


print(get_match())


def accept_match():
    # if choose this go to chat page*******SEE TRELLO PAGE*******
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

