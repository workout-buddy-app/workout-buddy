from db_management import get_db_connection
import time

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
            print(result)
    return result
    # needs to select one profile, not the current user ??
    # cannot repeat matches in a session
    # should randomise XX
    # needs at least to get name/username, picture, and bio XX


def accept_match():
    time.sleep(1)
    print("You are being redirected to your match's profile page")
    print("following others shows your interest!")
    time.sleep(1)
    print("They will receive a notification that contains a link to your profile")
    print("They will also receive your contact information")
    time.sleep(1)
    print("REMEMBER: be safe and kind! ^_^")
    # if choose this go to chat page*******SEE TRELLO PAGE*******
    # what about consent from the other person? or would it just ping them
    # print a warning message before redirection



def reject_match():
    # if choose this, cycle back into get_match
    pass


def quit_matching():
    # may not  need this as is webpage????
    # returns user to dashboard page or homepage
    pass


def user_interface():
    matches = 0
    print("Start finding buddies!")  # on html??
    while True:
        get_match()
        print()
        print("Please select an option:")
        print()
        print("[1] ACCEPT MATCH")
        print("[2] find someone else to connect with")
        print("[3] quit and return to your dashboard")
        action = input("Please select a button (for this select a number):  ")

        if action == '1':
            accept_match()
            break

        elif action == '2':
            print()

        elif action == '3':
            print("redirecting, please wait....")
            time.sleep(1)
            quit_matching()
            break

        else:
            print("Sorry, that wasn't one of the options. Please try again.")






def push_notification_to_accepted_match():
    pass


user_interface()

