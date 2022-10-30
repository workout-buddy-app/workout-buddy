from datetime import date



def is_over_eighteen(date_birth):
    """
    Checks the users age from date of birth form entry.
    If user is over 18, sign up can continue and return True.
    If user is under 18, error shows.
    """
    today = date.today()
    age = today.year - date_birth.year - ((today.month, today.day) < (date_birth.month, date_birth.day))
    return True if age >= 18 else False