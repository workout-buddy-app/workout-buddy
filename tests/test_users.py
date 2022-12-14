from unittest import TestCase, mock, main
from database.users import email_available, get_user_by_id, get_user_with_credentials


def get_mock_db_cursor(fetchone_return_value=None, fetchall_return_value=None):
    return mock.Mock(
        __enter__=lambda _: mock.Mock(
            execute=lambda query, params: None,
            fetchone=lambda: fetchone_return_value,
            fetchall=lambda: fetchall_return_value,
        ),
        __exit__=lambda *args: None,
    )


def get_mock_db_connection(mock_db_cursor):
    return mock.Mock(
        __enter__=lambda _: mock.Mock(
            cursor=lambda **kwargs: mock_db_cursor,
        ),
        __exit__=lambda *args: None,
    )


class TestUsers(TestCase):

    def test_email_available(self):
        test_email = 'test@test.com'
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = email_available(test_email)
            self.assertTrue(result)

    def test_check_email_available_with_unavailable_email(self):
        test_email = 'test@test.com'
        mock_user_id = 1
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user_id)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = email_available(test_email)
            self.assertFalse(result)

    def test_get_user_with_credentials(self):
        test_email = 'lynsay@gmail.com'
        test_password = 'password'
        mock_user = {'user_id': 1, 'name': 'Lynsay', 'email': 'lynsay@gmail.com', 'hashed_password': b'$2b$12$p9kwwch.CiFLvrm7IAOOXOcXvkm8S/RG8b14tfAF4IXBVoCkXnx/W'}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = get_user_with_credentials(test_email, test_password)
            self.assertEqual(result, mock_user)

    def test_get_user_without_credentials(self):
        test_email = 'idonotworkout@gmail.com'
        test_password = 'wrong'
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = get_user_with_credentials(test_email, test_password)
            self.assertIsNone(result)

    def test_get_user_by_id(self):
        test_user_id = 1
        mock_user = {'user_id': test_user_id, 'name': 'Lynsay', 'email': 'lynsay@gmail.com'}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = get_user_by_id(test_user_id)
            self.assertEqual(result, mock_user)

    def test_get_public_profile_data(self):
        test_user_id = 2
        test_about = 'I love to work out!'
        test_location = 'Belfast'
        mock_user = {'user_id': test_user_id, 'name': 'Lynsay', 'about': test_about, 'location': test_location}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = get_user_by_id(test_user_id)
            self.assertEqual(result, mock_user)


if __name__ == '__main__':
    main()
