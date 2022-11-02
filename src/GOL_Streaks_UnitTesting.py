import unittest
from unittest import mock
from mock import patch
from GOL_Streaks_Functions import TheUserStreak, _connect_to_db, db_connection_decorator
from db_functions import _connect_to_db, db_connection_decorator

class TestLastLogin(unittest.TestCase):

    def test_returnsLastDateValueIfLastLoginExistsInDB(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1')
        self.assertEqual(self.TUS.get_last_login(), '2022-11-01')

    def test_returnsCurrentDateIfDBDateIsNone(self):
        self.TUS = TheUserStreak(2, 'Username', 'freddy95')
        self.assertEqual(self.TUS.get_last_login(), '2022-11-01')


class TestGetExistingUserStreak(unittest.TestCase):

    def test_returnsUserStreakIfExistsInDB(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1')
        self.assertEqual(self.TUS.get_existing_user_streak(), 1)

    def test_returns1IfDBEntryIsEqualToNone(self):
        self.TUS = TheUserStreak(2, 'Username', 'freddy95')
        self.assertEqual(self.TUS.get_existing_user_streak(), 1)


class TestDateDifference(unittest.TestCase):

    def test_returnsUserCorrectDurationIfDateSuppliedByDB(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1', last_login='2022-10-31')
        self.assertEqual(self.TUS.calculate_login_diff(), 'Days since last login: 1')

    def test_raisesAnErrorIfLoginDifferenceIsLessThanZero(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1', last_login='2022-11-02')
        with self.assertRaises(ValueError) as context:
            self.TUS.calculate_login_diff()
            self.assertTrue('System error. Unable to calculate time since last logged in. Please try again later.' in context.exception)

    # def test_raisesAnErrorIfWrongFormat(self):
    #     with self.assertRaises(TypeError):
    #         self.TUS = TheUserStreak(1, 'Username', 'cobrien1', last_login='31-10-2022')
    #         self.TUS.calculate_login_diff()


class TestUserStreakAndDateUpdate(unittest.TestCase):

    def test_DBIsUpdatedIfLoginDifferenceIsEqualToOne(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1', login_difference=1)
        self.assertEqual(self.TUS.update_userstreak_and_last_login(), "Thanks for joining today! Your streak goes up!")

    def test_DBIsUpdatedIfLoginDifferenceIsGreaterThanOne(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1', login_difference=12)
        self.assertEqual(self.TUS.update_userstreak_and_last_login(), "Nice to see you! It's been a long time.")

    def test_DBIsUpdatedIfLoginDifferenceIsZero(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1', login_difference=0)
        self.assertEqual(self.TUS.update_userstreak_and_last_login(), "Keep up the hard work. \nDont forget to join us tomorrow too!")


    # def test_DBIsUpdatedIfLoginDifferenceIsNeg(self):
    #     with self.assertRaises(ValueError):
    #         self.TUS = TheUserStreak(1, 'Username', 'cobrien1', login_difference=-abs(10))
    #         self.TUS.update_userstreak_and_last_login()

    # NO NEED TO TEST FOR FLOATS AS TIMEDELTA-DAYS FUNCTION WILL ALWAYS PRODUCE INTEGER.

class TestUserStreaksDisplayFunction(unittest.TestCase):
    def test_ViewingUserStreak(self):
        self.TUS = TheUserStreak(1, 'Username', 'cobrien1')
        self.assertEqual(self.TUS.display_user_streak(), "Gift of Learning Streak: 1 Day(s).")


if __name__ == '__main__':
    unittest.main()