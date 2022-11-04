from unittest import TestCase, mock, main
import user_management


def get_mock_db_cursor(fetchone_return_value=None, fetchall_return_value=None):
    return mock.(
        __enter__=lambda _: mock.(
            execute=lambda query, params: None,
            fetchone=lambda: fetchone_return_value,
            fetchall=lambda: fetchall_return_value,
        ),
        __exit__=lambda *args: None,
    )


def get_mock_db_connection(mock_db_cursor):
    return mock.(
        __enter__=lambda _: mock.Mock(
            cursor=lambda **kwargs: mock_db_cursor,
        ),
        __exit__=lambda *args: None,
    )


class TestUserManagement(TestCase):

    def test_email_available(self):
        test_email = 'a@b.com'
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.email_available(test_email)
            self.assertTrue(result)

    def test_check_email_not_in_use_with_unavailable_email(self):
        test_email = 'a@b.com'
        mock_user_id = 1
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user_id)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.email_available(test_email)
            self.assertFalse(result)

    def test_get_user_by_id(self):
        test_user_id = X
        mock_user = {'full_name': 'XXX', 'email_address': 'XXX@gmail.com')}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.get_user_by_id(test_user_id)
            self.assertEqual(result, mock_user)

    def test_get_user_with_credentials(self):
        test_email = 'lynsay@gmail.com'
        test_password = 'P@55word'
        mock_user_id = 3
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value={'user_id': mock_user_id})
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.get_user_id_with_credentials(test_email, test_password)
            self.assertEqual(result, mock_user_id)

    def test_get_user_without_credentials(self):
        test_email = 'idonotworkout@gmail.com'
        test_password = 'wrong'
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with mock.patch('mysql.connector.connect', return_value=mock_db_connection):
            result = user_management.check_login_details(test_email, test_password)
            self.assertIsNone(result)


if __name__ == '__main__':
    main()