from unittest import TestCase
from datetime import datetime
from mock import patch, Mock, MagicMock
from gol_streaks_functions import TheUserStreak
from dictionary_api_functions import show_word_and_definition
from db_functions import check_if_valid_password, check_if_valid_username, check_if_valid_name, check_if_valid_email, check_if_valid_date

# Testing the word and definition function that prints a specific word and it's definition form the API when it's searched for via user input
class TestWordAndDefinition(TestCase):

    # These test if a user enters a word to search that does exist in the api
    def test_word_that_exists_in_API1(self):
        self.assertEqual(show_word_and_definition("House"), "The Word : House .  The Definition : A structure built or serving as an abode of human beings..")

    def test_word_that_exists_in_API2(self):
        self.assertEqual(show_word_and_definition("Socks"), "The Word : Socks .  The Definition : A knitted or woven covering for the foot..")

    # This tests if a user enters a word to search that doesn't exist in the api
    def test_incorrect_functionality(self):
        self.assertEqual(show_word_and_definition("hdjhsd"), "This word does not exist in the dictionary.")


# USER REGISTRATION TESTS

# A that a user email input has an @ symbol
class TestEmailValidation(TestCase):

    # Email inputs must have an @ symbol
    def test_valid_email(self):
        self.assertEqual(check_if_valid_email("gemma@gmail.com"), True)

    def test_invalid_email(self):
        self.assertEqual(check_if_valid_email("gemmagmail.com"), False)


# User input date format must be dd-mm-yyyy
class TestDateValidation(TestCase):
    def test_valid_date(self):
        self.assertEqual(check_if_valid_date("27-08-2000"), True)

    def test_invalid_date(self):
        self.assertEqual(check_if_valid_date("27-08-00"), False)





# Testing the password validation function
class TestPasswordValidation(TestCase):

    def test_valid_password(self):
        self.assertEqual(check_if_valid_password("Rebecca123!"), True)

    def test_invalid_password(self):
        self.assertEqual(check_if_valid_password("password"), False)

    # Passwords can not be empty
    def test_invalid_empty_password(self):
        self.assertEqual(check_if_valid_password(""), False)

    # Passwords need at least one number
    def test_valid_password_with_a_number(self):
        self.assertEqual(check_if_valid_password("Freddy123@"), True)

    def test_invalid_password_without_a_number(self):
        self.assertEqual(check_if_valid_password("Freddy@"),False)

    # Password need at least one Uppercase and one lower case letter
    def test_valid_password_with_upper_and_lowercase(self):
        self.assertEqual(check_if_valid_password("SamAntah123@"), True)

    def test_invalid_password_without_upper_and_lowercase(self):
        self.assertEqual(check_if_valid_password("samantha123@"), False)

    # Passwords need at least one special symbol:
    def test_valid_password_with_at_least_one_symbol(self):
        self.assertEqual(check_if_valid_password("Pinapple123@?"), True)

    def test_invalid_password_without_any_symbols(self):
        self.assertEqual(check_if_valid_password("Pinapple123"), False)

    def test_invalid_password_with_dashes_or_underscores(self):
        self.assertEqual(check_if_valid_password("Pinapple123_"), False)
        self.assertEqual(check_if_valid_password("Pinapple123-"), False)

    # Passwords should not be shorter than 6 characters
    def test_invalid_password_shorter_than_6(self):
        self.assertEqual(check_if_valid_password("Pi3@"), False)

    # Passwords should not be longer than 20 characters
    def test_invalid_password_longer_than_20(self):
        self.assertEqual(check_if_valid_password("Pinapplepen123!Oranges"), False)





# Testing the username validation function
class TestUsernameValidation(TestCase):

    def test_valid_username(self):
        self.assertEqual(check_if_valid_username("Gammy"), True)

    def test_valid_username(self):
        self.assertEqual(check_if_valid_username("Gammy"), True)

    # Usernames can not be empty
    def test_invalid_empty_username(self):
        self.assertEqual(check_if_valid_username(""), False)

    # Usernames are not allowed to be shorter than 5
    def test_invalid_username_length_below_4(self):
        self.assertEqual(check_if_valid_username("Ahd5"), False)

    # Usernames are not allowed to be longer than 21
    def test_invalid_username_length_above_21(self):
        self.assertEqual(check_if_valid_username("D123456789112345678911"), False)

    # Usernames are only allowed the symbols underscore(_) and dash (-)
    def test_invalid_username_symbols(self):
        self.assertEqual(check_if_valid_username("Ahhud!"), False)

    # Usernames must start with a letter
""" def test_invalid_username_not_starting_with_letter(self):
        self.assertEqual(check_if_valid_username("1Gimmy"), False)"""




class TestNameValidation(TestCase):

    # The name can't include any number, only letters
    def test_valid_name_letters_only(self):
        self.assertEqual(check_if_valid_name("Daniella"), True)

    def test_invalid_name_letters_and_numbers(self):
        self.assertEqual(check_if_valid_name("123Daniella"), False)

    # The name can't be shorter than 2
    def test_invalid_name_shorter_than_2(self):
        self.assertEqual(check_if_valid_name("D"), False)

    def test_valid_name_longer_than_2(self):
        self.assertEqual(check_if_valid_name("Dan"), True)

    # The name can't be longer than 25
    def test_invalid_name_longer_than_25(self):
        self.assertEqual(check_if_valid_name("DaniellaDaniellaDaniellaDaniella"), False)

    def test_valid_name_shorter_than_25(self):
        self.assertEqual(check_if_valid_name("Dani"), True)

class TestLastLogin(TestCase):

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




class TestGetExistingUserStreak(TestCase):
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



class TestUserStreakAndDateUpdate(TestCase):

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



class TestUserStreaksDisplayFunction(TestCase):
    def test_viewing_userstreak_value(self):
        with patch('mysql.connector.connect') as mock_db_connection_decorator:
            connection = mock_db_connection_decorator.return_value
            cur = connection.cursor.return_value
            cur.fetchall.return_value = [('2',)]

            # INITIALISING ATTRIBUTES
            self.TUS = TheUserStreak('Username', 'cobrien1')
            # TEST ASSERTION
            self.assertEqual(self.TUS.display_user_streak(), "Gift of Learning Streak: 2 Day(s).")



class TestUserMonthlyUserIDFunction(TestCase):

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


class TestUserMonthlySearchedWordCount(TestCase):

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


class TestDisplayMonthlyAnalytics(TestCase):

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

