import unittest


class TestAdventOfCodeDay05(unittest.TestCase):
    def testIsNice_IsNiceDifferentVowels_ReturnsTrue(self):
        actual = is_nice("ugknbfddgicrmopn")
        self.assertTrue(actual)

    def testIsNice_IsNiceOnlyThreeOfSameVowel_ReturnsTrue(self):
        actual = is_nice("aaa")
        self.assertTrue(actual)

    def testIsNice_IsNotNiceNoDoubleLetter_ReturnsFalse(self):
        actual = is_nice("jchzalrnumimnmhp")
        self.assertFalse(actual)

    def testIsNice_IsNotNiceContainsXY_ReturnsFalse(self):
        actual = is_nice("haegwjzuvuyypxyu")
        self.assertFalse(actual)

    def testIsNice_IsNotNiceOnlyOneVowel_ReturnsFalse(self):
        actual = is_nice("haegwjzuvuyypxyu")
        self.assertFalse(actual)

    def testIsNice2_IsNiceContainsPair_ReturnsTrue(self):
        actual = is_nice2("xxyxx")
        self.assertTrue(actual)

    def testIsNice2_IsNiceStartOfPairIsInMiddle_ReturnsTrue(self):
        actual = is_nice2("asbsddyrfhydd")
        self.assertTrue(actual)

    def testIsNice2_IsNaughtyNoPair_ReturnsFalse(self):
        actual = is_nice2("ieodomkazucvgmuy")
        self.assertFalse(actual)

    def testIsNice2_IsNicePairsAtEndOfString_ReturnsTrue(self):
        actual = is_nice2("absdyryfhydldl")
        self.assertTrue(actual)

    def testIsNice2_IsNaughtyNoRepeatLetter_ReturnsFalse(self):
        actual = is_nice2("uurcxstgmygtbstg")
        self.assertFalse(actual)

    def testIsNice2_IsNiceRepeatAtEndOfString_ReturnsTrue(self):
        actual = is_nice2("ieodmkazoducvgmuyu")
        self.assertTrue(actual)

    def testIsNice2_IsNiceSameLetterQuartet_ReturnsTrue(self):
        actual = is_nice2("dddd")
        self.assertTrue(actual)

    def testIsNice2_IsNaughtySameLetterTriplet_ReturnsFalse(self):
        actual = is_nice2("fff")
        self.assertFalse(actual)


def is_nice2(string_value):
    return has_pair_of_two_letters(string_value) and has_repeating_letter(string_value)


def has_pair_of_two_letters(string_value):
    length = len(string_value)
    for i in range(0, length - 3):
        test_pair = string_value[i:i + 2]
        remaining_string = string_value[i + 2:length]
        if remaining_string.find(test_pair) >= 0:
            return True
    return False


def has_repeating_letter(string_value):
    length = len(string_value)
    for i in range(length - 2):
        current_char = string_value[i]
        test_char = string_value[i + 2]
        if current_char == test_char:
            return True
    return False



def is_nice(string_value):
    return has_at_least_three_vowels(string_value) and has_double_letter(string_value) and does_not_have_naughty_string(string_value)


def has_at_least_three_vowels(string_value):
    return (string_value.count("a") +string_value.count("e") + string_value.count("o") + string_value.count("u") + string_value.count("i")) >= 3


def has_double_letter(string_value):
    last_character = ""
    for character in string_value:
        if last_character == character:
            return True
        last_character = character


def does_not_have_naughty_string(string_value):
    return string_value.find("ab") < 0 and string_value.find("cd") < 0 and string_value.find("pq") < 0 and string_value.find("xy") < 0


def main():
    nice_string_count = 0
    nice_string_count2 = 0
    with open("input/day_05.txt", "r") as inputFile:
        for input_line in inputFile:
            if is_nice(input_line):
                nice_string_count += 1
            if is_nice2(input_line):
                nice_string_count2 += 1
    print("nice string count: ", nice_string_count)
    print("nice string count 2: ", nice_string_count2)


if __name__ == "__main__":
    main()