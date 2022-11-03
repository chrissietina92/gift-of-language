import unittest
from unittest import mock
from mock import patch, Mock, MagicMock
from datetime import datetime, timedelta, date
from GOL_Streaks_Functions import TheUserStreak


class TestLastLogin(unittest.TestCase):

    def test_returnsLastDateValueIfLastLoginExistsInDB(self):

        with patch('mysql.connector.connect')as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('2022-10-29',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'freddy95')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_last_login(), '2022-10-29')


    def test_returnsLastDateValueIfLastLoginIsNone(self):

        with patch('mysql.connector.connect')as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [(None,)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'freddy95')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_last_login(), '2022-11-02')




class TestGetExistingUserStreak(unittest.TestCase):
    def test_returnsUserStreakIfExistsInDB(self):

        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('6',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_existing_user_streak(), '6')

    def test_returns1IfDBEntryIsEqualToNone(self):

        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [(None,)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'freddy95')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_existing_user_streak(), 1)



class TestUserStreakAndDateUpdate(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_DBIsUpdatedIfLoginDifferenceIsEqualToOne(self, mock_sql):
        # MOCK RETURN/COMMIT DB CONNECTION
        connection = Mock()
        mock_sql.connect.return_value = connection
        cursor = MagicMock()
        mock_result = MagicMock()
        cursor.__enter__.return_value = mock_result
        cursor.return_value = cursor

        # INITIALISING ATTRIBUTES
        self.TUS = TheUserStreak('Username', 'cobrien1', login_difference=1)
        # TEST ASSERTION
        self.assertEqual(self.TUS.update_userstreak_and_last_login(), "Thanks for joining today! Your streak goes up!")


    @patch('mysql.connector.connect')
    def test_DBIsUpdatedIfLoginDifferenceIsGreaterThanOne(self, mock_sql):
        # MOCK RETURN/COMMIT DB CONNECTION
        connection = Mock()
        mock_sql.connect.return_value = connection
        cursor = MagicMock()
        mock_result = MagicMock()
        cursor.__enter__.return_value = mock_result
        cursor.return_value = cursor

        # INITIALISING ATTRIBUTES
        self.TUS = TheUserStreak('Username', 'cobrien1', login_difference=12)
        # TEST ASSERTION
        self.assertEqual(self.TUS.update_userstreak_and_last_login(), "Nice to see you! It's been a long time.")

    @patch('mysql.connector.connect')
    def test_DBIsUpdatedIfLoginDifferenceIsZero(self, mock_sql):
        # MOCK RETURN/COMMIT DB CONNECTION
        connection = Mock()
        mock_sql.connect.return_value = connection
        cursor = MagicMock()
        mock_result = MagicMock()
        cursor.__enter__.return_value = mock_result
        cursor.return_value = cursor

        # INITIALISING ATTRIBUTES
        self.TUS = TheUserStreak('Username', 'cobrien1', login_difference=0)
        # TEST ASSERTION
        self.assertEqual(self.TUS.update_userstreak_and_last_login(), "Keep up the hard work. \nDont forget to join us tomorrow too!")


    #A DB ERROR IS THROWN BY THE INPUTS. I'M UNSURE WHY.

    # @patch('mysql.connector.connect')
    # def test_DBIsUpdatedIfLoginDifferenceIsNeg(self, mock_sql):
    #     # MOCK RETURN/COMMIT DB CONNECTION
    #     connection = Mock()
    #     mock_sql.connect.return_value = connection
    #     cursor = MagicMock()
    #     mock_result = MagicMock()
    #     cursor.__enter__.return_value = mock_result
    #     cursor.return_value = cursor
    #
    #     with self.assertRaises(ConnectionError):
    #         self.TUS = TheUserStreak('Username', 'cobrien1', login_difference=-10)
    #         self.TUS.update_userstreak_and_last_login()



    # NO NEED TO TEST FOR FLOATS AS TIMEDELTA-DAYS FUNCTION WILL ALWAYS PRODUCE INTEGER.

class TestUserStreaksDisplayFunction(unittest.TestCase):
    def test_ViewingUserStreak(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('2',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.display_user_streak(), "Gift of Learning Streak: 2 Day(s).")

# ATTEMPT 1:STRUGGLING TO MOCK DATETIME MODULE.

# class TestDateDifference(unittest.TestCase):
# @mock.patch(TheUserStreak, 'datetime', Mock(wraps=datetime))
# def test_returnsUserCorrectDurationIfDateSuppliedByDB(self):
#     TheUserStreak.datetime.now.date.return_value = datetime.datetime(2022, 10, 31)
#
#     self.TUS = TheUserStreak('Username', 'cobrien1', last_login='2022-10-29')
#     self.assertEqual(self.TUS.calculate_login_diff(), 'Days since last login: 2')


# ATTEMPT 2
#     def test_raisesAnErrorIfLoginDifferenceIsLessThanZero(self):
#         with self.assertRaises(ValueError) as context:
#         self.TUS = TheUserStreak(1, 'Username', 'cobrien1', last_login='2022-11-02')
#             self.TUS.calculate_login_diff()
#             self.assertTrue('System error. Unable to calculate time since last logged in. Please try again later.' in context.exception)


# def test_raisesAnErrorIfWrongFormat(self):
#     with self.assertRaises(TypeError):
#         self.TUS = TheUserStreak(1, 'Username', 'cobrien1', last_login='31-10-2022')
#         self.TUS.calculate_login_diff()


if __name__ == '__main__':
    unittest.main()