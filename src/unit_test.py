from unittest import TestCase
from db_functions import check_if_valid_password, check_if_valid_username, check_if_valid_name,check_if_valid_email
from dictionary_api_functions import show_word_and_definition


# A that a user email input has an @ symbol
class TestEmailValidation(TestCase):

    # Email inputs must have an @ symbol
    def test_valid_email(self):
        self.assertEqual(check_if_valid_email("gemma@gmail.com"), True)

    def test_invalid_email(self):
        self.assertEqual(check_if_valid_email("gemmagmail.com"), False)

class TestDateValidation(TestCase):

    # A user email input must have an @ symbol
    def test_valid_email(self):
        self.assertEqual(check_if_valid_email("gemma@gmail.com"), True)

    def test_invalid_email(self):
        self.assertEqual(check_if_valid_email("gemmagmail.com"), False)



# Testing the word and definition function that prints a specific word and it's definition form the API when it's searched for via user input
class TestWordAndDefinition(TestCase):

    # These test if a user enters a word to search that does exist in the api
    def test_word_that_exists_in_API1(self):
        self.assertEqual(show_word_and_definition("House"), True)

    def test_word_that_exists_in_API2(self):
        self.assertEqual(show_word_and_definition("Socks"), True)

    # This tests if a user enters a word to search that doesn't exist in the api
    def test_incorrect_functionality(self):
        self.assertEqual(show_word_and_definition("hdjhsd"), False)



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



