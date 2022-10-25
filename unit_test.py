from unittest import TestCase, mock
from db_searched_words import check_if_word_in_database
from api import get_definition
from db_functions import does_user_exist
import daily_words
from daily_words import randomWordGenerator, searchAPIForRandomWord

class TestLearntWords(TestCase):
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