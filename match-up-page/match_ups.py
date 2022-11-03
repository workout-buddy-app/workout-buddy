from database.connection import get_db_connection
from app import view_own_profile, public_profile
import time


# need to get this checked
def get_match(current_user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT ud.user_id, ud.display_name, ud.about, ud.location
                                FROM user_data AS ud
                                WHERE ud.user_id NOT IN (SELECT mu.matched_user_id 
                                                            FROM matched_users AS mu 
                                                            WHERE mu.current_user_id = %s)
                                ORDER BY rand() LIMIT 1""", [current_user_id])
            result = cursor.fetchone()
            print(result)
    return result


def accept_match():
    """Should connect to database and insert the matched pair
    :param current_user_id, matched_user_id
    use the code below possibly"""
    # with get_db_connection() as connection:
    #     with connection.cursor(dictionary=True) as cursor:
    #         cursor.execute("""INSERT INTO matched_users
    #                         (current_user_id, matched_user_id)
    #                         VALUES
    #                         (%, %)"""[current_user_id, matched_user_id]
    #                        )
    time.sleep(1)
    print()
    print("You are being redirected to your match's profile page")
    print("following others shows your interest!")
    print()
    time.sleep(3)
    push_notification_to_accepted_match()
    print("REMEMBER: be safe and kind! ^_^")
    time.sleep(3)
    public_profile  # this is to show what the front end should do


def reject_match():
    print("Please wait, we are finding your next buddy!")
    time.sleep(1)


def quit_matching():
    print("redirecting, please wait...")
    time.sleep(1)
    view_own_profile  # this is to show what the front end should do


def user_interface():
    print("Start finding buddies!")
    while True:
        get_match(2)
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
            quit_matching()
            break

        else:
            print("Sorry, that wasn't one of the options. Please refresh and try again.")
            break


def push_notification_to_accepted_match():
    print("They will receive a notification that contains a link to your profile")
    print("They will also receive your contact information")
    print()
    time.sleep(3)
    # how on earth do I send something to another user
    pass


if __name__ == '__main__':
    user_interface()

