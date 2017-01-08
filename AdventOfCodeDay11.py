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

    def testIsValidPassword_WhenNoThreeStraight_ReturnsFalse(self):
        actual = is_valid_password("abdffaa")
        self.assertFalse(actual)

    def testIsValidPassword_WhenTwoSetsOfTwoStraights_ReturnsFalse(self):
        actual = is_valid_password("abdffcdaa")
        self.assertFalse(actual)

    def testIsValidPassword_WhenOnlyThreeStraightCharacters_ReturnsTrue(self):
        actual = is_valid_password("abcffaa")
        self.assertTrue(actual)

    def testIsValidPassword_WhenContainsi_ReturnsFalse(self):
        actual = is_valid_password("abcffiaa")
        self.assertFalse(actual)

    def testIsValidPassword_WhenContainso_ReturnsFalse(self):
        actual = is_valid_password("abcffoaa")
        self.assertFalse(actual)

    def testIsValidPassword_WhenContainsl_ReturnsFalse(self):
        actual = is_valid_password("abcfflaa")
        self.assertFalse(actual)

    def testIsValidPassword_WhenSinglePair_ReturnsFalse(self):
        actual = is_valid_password("abcffnz")
        self.assertFalse(actual)

    def testIsValidPassword_WhenThreeCharactersInRow_ReturnsFalse(self):
        actual = is_valid_password("abcdeggg")
        self.assertFalse(actual)

    def testIsValidPassword_WhenThreeSequenceOverlapsTwoPairs_ReturnsTrue(self):
        actual = is_valid_password("ghjaabcc")
        self.assertTrue(actual)

    def testGetNextPassword_When_abcdefgh_Returns_abcdffaa(self):
        actual = get_next_valid_password("abcdefgh")
        self.assertEqual(actual, "abcdffaa")

    def testGetNextPassword_When_ghijklmn_Returns_ghjaabcc(self):
        actual = get_next_valid_password("ghijklmn")
        self.assertEqual(actual, "ghjaabcc")

    def testIncrementInvalidCharacter_When_ghijklmn_Returns_ghjaaaaa(self):
        actual = increment_invalid_character("ghijklmn")
        self.assertEqual(actual, "ghjaaaaa")


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


def is_valid_password(password):
    invalid_characters = "iol"
    if any(char in password for char in invalid_characters):
        return False
    last_character_ord = 0
    characters_in_sequence_count = 1
    sequence_of_three_found = False
    character_pairs_count = 0
    in_character_run = False
    for character in password:
        character_ord = ord(character)
        if character_ord == last_character_ord:
            if not in_character_run:
                in_character_run = True
                character_pairs_count += 1
        else:
            in_character_run = False
        if character_ord == (last_character_ord + 1):
            characters_in_sequence_count += 1
        else:
            characters_in_sequence_count = 1
        if characters_in_sequence_count == 3:
            sequence_of_three_found = True
        last_character_ord = character_ord
    return sequence_of_three_found and (character_pairs_count >= 2)


def increment_invalid_character(password):
    i_index = password.find('i')
    if i_index >= 0:
        return increment_password_by_position(password, i_index)
    l_index = password.find('l')
    if l_index >= 0:
        return increment_password_by_position(password, l_index)
    o_index = password.find('o')
    if o_index >= 0:
        return increment_password_by_position(password, o_index)


def increment_password_by_position(password, position):
    length = len(password)
    next_password = increment_password(password[0:position + 1])
    next_password += 'a' * (length - position - 1)
    return next_password


def increment_to_next_valid_password(password):
    invalid_characters = "iol"
    if any(char in password for char in invalid_characters):
        return increment_invalid_character(password)
    return increment_password(password)


def get_next_valid_password(password):
    next_password = increment_to_next_valid_password(password)
    while not is_valid_password(next_password):
        next_password = increment_to_next_valid_password(next_password)
    return next_password


def main():
    current_password = "cqjxjnds"
    next_valid_password = get_next_valid_password(current_password)
    print(next_valid_password)
    next_valid_password = get_next_valid_password(next_valid_password)
    print(next_valid_password)


if __name__ == '__main__':
    main()