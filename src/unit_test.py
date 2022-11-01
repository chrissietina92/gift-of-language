from unittest import TestCase
from db_functions import check_if_valid_password, check_if_valid_username, check_if_valid_name
from dictionaryapi_functions import show_word_and_definition


# use mocking to test this
"""class TestLearntWords(TestCase):
    def test_check_in_database_true(self):
        self.assertTrue(check_if_word_in_database(word = 'House'))

    def test_check_in_database_true(self):
        self.assertTrue(check_if_word_in_database(word = 'play'))

    def test_check_in_database_false(self):
        excepted = False
        result = check_if_word_in_database('eat')
        self.assertEqual(excepted, result)

    def test_check_in_database_false(self):
        excepted = False
        result = check_if_word_in_database('go')
        self.assertEqual(excepted, result)

class TestGetDefinitionFromAPI(TestCase):
    def test_get_right_definition_from_API(self):
        excepted = 'Each of the seven major bodies which move relative to the fixed stars in the night sky—the Moon, Mercury, Venus, the Sun, Mars, Jupiter and Saturn.'
        result = get_definition('planet')
        self.assertEqual(excepted, result)

    def test_get_wrong_definition_from_API(self):
        excepted = 'Each of the seven major bodies which move relative to the fixed stars in the night sky—the Moon, Mercury, Venus, the Sun, Mars, Jupiter and Saturn.'
        result = get_definition('word')
        self.assertNotEqual(excepted, result)

class TestCheckUsers(TestCase):
    def test_does_user_exist_True(self):
        self.assertTrue(does_user_exist(column='Username', value='anna123'))

    def test_does_user_exist_True(self):
        self.assertTrue(does_user_exist(column='Email', value='hayley99@email.com'))

    def test_does_user_exist_False(self):
        self.assertFalse(does_user_exist(column='Username', value='john342'))

    def test_does_user_exist_False(self):
        self.assertFalse(does_user_exist(column='Username', value='my_friend1'))

class TestDailyWords(TestCase):

    def test_searchAPIForRandomWord_correct_res(self):
        expected = ('Word: house', 'Definition: A structure built or serving as an abode of human beings.')
        result = searchAPIForRandomWord(randomWord='House')
        self.assertEqual(expected, result)

    def test_searchAPIForRandomWord_wrong_res(self):
        expected = ('Word: play', 'Definition: A structure built or serving as an abode of human beings.')
        result = searchAPIForRandomWord(randomWord='Play')
        self.assertNotEqual(expected, result)

    @mock.patch.object(daily_words, 'searchAPIForRandomWord')
    def test_randomWordGenerator_works(self, mock_searchAPIForRandomWord):
        mock_searchAPIForRandomWord.return_value = ('Word: accountants', 'Definition: One who renders account; one accountable.')
        expected = ('Word: accountants', 'Definition: One who renders account; one accountable.')
        result = randomWordGenerator()
        self.assertEqual(expected, result)

    @mock.patch.object(daily_words, 'searchAPIForRandomWord')
    def test_randomWordGenerator_not_working(self, mock_searchAPIForRandomWord):
        mock_searchAPIForRandomWord.return_value = ('Word: accountants')
        expected = ('Word: accountants', 'Definition: One who renders account; one accountable.')
        result = randomWordGenerator()
        self.assertNotEqual(expected, result)

class TestUserPasswordMatch(TestCase):
    def test_user_password_match(self):
        self.assertTrue(username_and_password_match(column='Username', value='anna123', password_value='anna123'))

    def test_user_password_match(self):
        self.assertTrue(username_and_password_match(column='Email', value='jcal@email.com', password_value='cat123'))

"""


# Test to check if a words name and its definition is printed when user searches it
class TestWordAndDefinition(TestCase):

    def test_correct_functionality(self):
        self.assertEqual(show_word_and_definition("House"),"The definition of House is: A structure built or serving as an abode of human beings.")

    def test_correct_functionality2(self):
        self.assertEqual(show_word_and_definition("Socks"),"The definition of Socks is: A knitted or woven covering for the foot.")


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



class TestUsernameValidation(TestCase):

    def test_valid_username(self):
        self.assertEqual(check_if_valid_username("Gammy"), True)

    def test_valid_username(self):
        self.assertEqual(check_if_valid_username("Gammy"), True)

    # Usernames can not be empty
    def test_invalid_empty_username(self):
        self.assertEqual(check_if_valid_username(""), False)

    # Usernames are not allowed to be shorter than 4
    def test_invalid_username_length_below_4(self):
        self.assertEqual(check_if_valid_username("Ahd"), False)

    # Usernames are not allowed to be longer than 20
    def test_invalid_username_length_above_20(self):
        self.assertEqual(check_if_valid_username("Sshjjdjcjjjrnnnsjfyyj"), False)

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



