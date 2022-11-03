import unittest
from unittest import mock
from mock import patch, Mock, MagicMock, PropertyMock
from datetime import datetime, timedelta, date
from GOL_Streaks_Functions import TheUserStreak


class TestLastLogin(unittest.TestCase):

    def test_returns_last_date_value_if_last_login_exists_in_DB(self):
        with patch('mysql.connector.connect')as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('2022-10-29',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'freddy95')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_last_login(), '2022-10-29')


    def test_returns_last_date_value_if_last_login_is_none(self):
        with patch('mysql.connector.connect')as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [(None,)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'freddy95')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_last_login(), datetime.now().date().strftime("%Y-%m-%d"))




class TestGetExistingUserStreak(unittest.TestCase):
    def test_returns_userstreak_if_a_value_exists_in_db(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('6',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_existing_user_streak(), '6')

    def test_returns_1_if_db_entry_is_equal_to_none(self):

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
    def test_db_is_updated_if_login_difference_is_equal_to_one(self, mock_sql):
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
    def test_db_is_updated_if_login_difference_is_greater_than_one(self, mock_sql):
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
    def test_db_is_updated_if_login_difference_is_equal_to_zero(self, mock_sql):
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


    # NO NEED TO TEST FOR FLOATS AS TIMEDELTA-DAYS FUNCTION WILL ALWAYS PRODUCE INTEGER.



class TestUserStreaksDisplayFunction(unittest.TestCase):
    def test_viewing_userstreak_value(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('2',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.display_user_streak(), "Gift of Learning Streak: 2 Day(s).")



class TestUserMonthlyUserIDFunction(unittest.TestCase):

    # USER ID IS AUTO INCREMENTED AND WILL NEVER BE NULL.
    def test_viewing_user_id(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [(3,)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_userid_by_column(), 3)


class TestUserMonthlySearchedWordCount(unittest.TestCase):

    # USER ID IS AUTO INCREMENTED AND WILL NEVER BE NULL.
    def test_getting_searched_word_monthly_count_if_entries_exist_in_db(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [("10",)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_month_total_searched_word_count(), '10')

    def test_getting_searched_word_monthly_count_if_entries_do_not_exist_in_db(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = []

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.get_month_total_searched_word_count(), 0)


class TestDisplayMonthlyAnalytics(unittest.TestCase):

    # NEW USER TEST/SOMEONE WHO HAS NOT SEARCHED AT ALL.
    def test_display_when_monthly_count_is_zero(self):
        self.TUS = TheUserStreak('Username', 'freddy95', streak_month=0)
        self.assertEqual(self.TUS.display_monthly_analytics(), 'You need to start using your dictionary more often, buddy.')

    def test_display_when_monthly_count_is_between_one_and_fifteen(self):
        self.TUS = TheUserStreak('Username', 'freddy95', streak_month=13)
        self.assertEqual(self.TUS.display_monthly_analytics(), "Well done, buddy.")

    def test_display_when_monthly_count_is_greater_than15(self):
        self.TUS = TheUserStreak('Username', 'freddy95', streak_month=100)
        self.assertEqual(self.TUS.display_monthly_analytics(), "You're a superstar!")


if __name__ == '__main__':
    unittest.main()

