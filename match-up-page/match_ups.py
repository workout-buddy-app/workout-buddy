from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from db_management import get_db_connection
from app import view_own_profile
import time


def get_match():
    # I think I need to add some sort of counter to each user, so they cannot be chosen in the same session?
    # i also need to somehow set the current user id, prob from app.py??
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT ud.display_name, ud.about, ud.location, ud.user_id 
                                FROM user_data AS ud
                                ORDER BY rand() LIMIT 1""")
            result = cursor.fetchone()
            # user_id = ud.user_id
            # if user_id != current_user:
                # print(result)
            print(result)  # but I don't want this to show the user id????
    return result
    # needs to select one profile, not the current user ??
    # cannot repeat matches in a session
    # should randomise XX
    # needs at least to get name/username, picture, and bio XX


def accept_match():
    time.sleep(1)
    print()
    print("You are being redirected to your match's profile page")
    print("following others shows your interest!")
    print()
    time.sleep(3)
    push_notification_to_accepted_match()
    print("REMEMBER: be safe and kind! ^_^")
    time.sleep(3)
    # some sort of redirection to a page that doesn't exist?


def reject_match():
    print("Please wait, we are finding your next buddy!")
    time.sleep(1)


def quit_matching():
    print("redirecting, please wait")
    time.sleep(1)
    view_own_profile


def user_interface():
    # I want this function/ page only accessible by logged-in users
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
    print("They will receive a notification that contains a link to your profile")
    print("They will also receive your contact information")
    print()
    time.sleep(3)
    # how on earth do I send something to another user
    pass


if __name__ == '__main__':
    user_interface()

