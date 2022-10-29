def get_user_details(user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            user = {'id': user_id, 'username': 'somebody', 'display_name': 'Some Body'}
            return user

