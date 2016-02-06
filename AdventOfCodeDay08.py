import unittest


class TestAdventOfCodeDay08(unittest.TestCase):
    def testCountCodeCharacters_NoEscapedCharacters_ReturnsCorrectValue(self):
        actual = count_code_characters(r'"abc"')
        self.assertEqual(actual, 5)

    def testCountInMemoryCharacters_NoEscapedCharacters_ReturnsCorrectValue(self):
        actual = count_in_memory_characters(r'"abc"')
        self.assertEqual(actual, 3)

    def testCountInMemoryCharacters_NoStartDoubleQuote_RaisesException(self):
        with self.assertRaises(Exception):
            count_in_memory_characters(r'abc"')

    def testCountInMemoryCharacters_NoEndDoubleQuote_RaisesException(self):
        with self.assertRaises(Exception):
            count_in_memory_characters(r'"abc')

    def testCountInMemoryCharacters_EscapedBackslash_ReturnsCorectValue(self):
        actual = count_in_memory_characters(r'"ab\\c"')
        self.assertEqual(actual, 4)

    def testCountInMemoryCharacters_EscapedDoubleQuote_ReturnsCorrectValue(self):
        actual = count_in_memory_characters(r'"abc\"defg\""')
        self.assertEqual(actual, 9)

    def testCountInMemoryCharacters_EscapedAsciiCodeAlone_ReturnsCorrectValue(self):
        actual = count_in_memory_characters(r'"\x27"')
        self.assertEqual(actual, 1)

    def testCountInMemoryCharacters_EscapedAsciiCode_ReturnsCorrectValue(self):
        actual = count_in_memory_characters(r'"abc\x27de"')
        self.assertEqual(actual, 6)

    def testCountInMemoryCharacters_WithWhitespace_IgnoresWhiteSpace(self):
        actual = count_in_memory_characters(r' "abc\x27def\\monkey\""    ')
        self.assertEqual(actual, 15)

    def testCountCodeCharacters_WithWhitespace_IgnoresWhitespace(self):
        actual = count_code_characters(r' "abc\x27def\\monkey\""    ')
        self.assertEqual(actual, 22)

    def testGetEncodedString_EmptyString_ReturnsCorrectString(self):
        actual = get_encoded_string(r'""')
        self.assertEqual(actual, r'"\"\""')

    def testGetEncodedString_NoEscapedCharacters_ReturnsCorrectString(self):
        actual = get_encoded_string(r'"abc"')
        self.assertEqual(actual, r'"\"abc\""')

    def testGetEncodedString_EscapedDoubleQuote_ReturnsCorrectString(self):
        actual = get_encoded_string(r'"aaa\"aaa"')
        self.assertEqual(actual, r'"\"aaa\\\"aaa\""')

    def testGetEncodedString_EscapedAsciiCode_ReturnsCorrectString(self):
        actual = get_encoded_string(r'"\x27"')
        self.assertEqual(actual, r'"\"\\x27\""')

    def testCountEncodedCharacters_WithWhitespace_ReturnsCorrectValue(self):
        actual = count_encoded_characters(r'    "aaa\"aaa"    ')
        self.assertEqual(actual, 16)


def count_code_characters(code_string):
    return len(code_string.strip())


def count_encoded_characters(code_string):
    test_string_encoded = get_encoded_string(code_string.strip())
    return len(test_string_encoded)


def get_encoded_string(code_string):
    encoded_string = r''
    for character in code_string:
        if character == '"':
            encoded_string += r'\"'
        elif character == '\\':
            encoded_string += r'\\'
        else:
            encoded_string += character
    return '"' + encoded_string + '"'


def count_in_memory_characters(code_string):
    test_string = code_string.strip()
    if test_string[0] != '"' or test_string[-1] != '"':
        raise Exception("String must begin and end with a double quote character: {0}".format(code_string))
    test_string = test_string[1:-1]
    in_escape_sequence = False
    count = 0
    for i in range(len(test_string)):
        if in_escape_sequence:
            if test_string[i] == 'x':
                count -= 2
            count += 1
            in_escape_sequence = False
        elif test_string[i] == '\\':
            in_escape_sequence = True
        else:
            count += 1
    return count


def main():
    total_code_character_count = 0
    total_in_memory_character_count = 0
    total_encoded_character_count = 0
    with open("input/day_08.txt", "r") as inputFile:
        for code_string in inputFile:
            total_code_character_count += count_code_characters(code_string)
            total_in_memory_character_count += count_in_memory_characters(code_string)
            total_encoded_character_count += count_encoded_characters(code_string)
    total_difference = total_code_character_count - total_in_memory_character_count
    total_encoded_difference = total_encoded_character_count - total_code_character_count
    print("total difference: ", total_difference)
    print("total encoded difference: ", total_encoded_difference)


if __name__ == '__main__':
    main()