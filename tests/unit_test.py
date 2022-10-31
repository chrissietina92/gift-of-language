from unittest import mock, TestCase
from src.db_searched_words import user_db
from src.api import get_definition
from src.db_functions import does_user_exist, new_user
from src import daily_words
from src.daily_words import randomWordGenerator, searchAPIForRandomWord
from src.Login_Interface_Python_Logic import username_and_password_match



class TestGiftOfLanguage(TestCase):

    @mock.patch("")



# use mocking to test this
class TestLearntWords(TestCase):
    @mock.patch.object(user_db, 'check_if_word_in_database')
    def test_check_in_database_true(self, mock_query):
        mock_query.return_value = "SELECT word FROM searched_words_user_4; "
        result = user_db.check_if_word_in_database(word = 'work')
        self.assertTrue(result)


    @mock.patch.object(user_db, 'userid')
    def test_2_check_in_database_true(self, mock_userid):
        mock_userid.return_value = 3
        result = user_db.check_if_word_in_database(word='play')
        self.assertTrue(result)

    #@mock.patch.object(user_db, 'userid')
    #def test_2_check_in_database_true(self, mock_userid):
    #    mock_userid.value = 1
    #    result = user_db.check_if_word_in_database(word='world')
    #    self.assertTrue(result)

    #@mock.patch(new_user, 'check_if_word_in_database')
    #def test_2_check_not_in_database(self, mock_query):
    #    mock_query.patch('builtins.input', side_effect= "SELECT word FROM searched_words_user_3; ")
    #    result = user_db.check_if_word_in_database(word='play')
    #    self.assertTrue(result)

    #def test_check_in_database_true(self):
    #    with mock.patch.object(new_user, "userid") as attr_mock:
    #        attr_mock.return_value = 4
     #    self.assertTrue(user.check_if_valid_username(word='work'))
    #def test_check_in_database_true(self):
    #    self.assertTrue(check_if_word_in_database(word = 'play'))

    #def test_check_in_database_false(self):
    #    excepted = False
    #    result = check_if_word_in_database('eat')
    #    self.assertEqual(excepted, result)

   # def test_check_in_database_false(self):
   #     excepted = False
   #     result = check_if_word_in_database('go')
   #     self.assertEqual(excepted, result)


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