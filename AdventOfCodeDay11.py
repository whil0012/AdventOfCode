import unittest


class TestAdventOfCodeDay11(unittest.TestCase):
    def testIncrementPassword_Whena_Returnsb(self):
        actual = increment_password("a")
        self.assertEqual(actual, "b")

    def testIncrementPassword_Whenaa_Returnsab(self):
        actual = increment_password("aa")
        self.assertEqual(actual, "ab")

    def testIncrementPassword_Whenaz_Returnsba(self):
        actual = increment_password("az")
        self.assertEqual(actual, "ba")

    def testIncrementPassword_Whenz_Returnsaa(self):
        actual = increment_password("z")
        self.assertEqual(actual, "aa")

    def testIncrementPassword_Whenazz_returnsbaa(self):
        actual = increment_password("azz")
        self.assertEqual(actual, "baa")

    def testIsValidPassword_WhenIsValid_ReturnsTrue(self):
        actual = is_valid_password("abcdffaa")
        self.assertTrue(actual)


def increment_character(old_char):
    return chr(ord(old_char) + 1)


def increment_password(old_password):
    if old_password == '':
        return 'a'
    old_char = old_password[-1]
    if old_char == 'z':
        return increment_password(old_password[0:-1]) + 'a'
    else:
        return old_password[0:-1] + increment_character(old_char)


def is_valid_password(param):
    return True