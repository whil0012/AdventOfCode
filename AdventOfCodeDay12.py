import unittest
import json


class TestAdventOfCodeDay12(unittest.TestCase):
    def test_sum_numbers_WhenNoNumbers_Returns0(self):
        actual = sum_numbers("[\"text\"]")
        self.assertEqual(actual, 0)

    def test_sum_numbers_WhenOneNumberInList_ReturnsNumber(self):
        actual = sum_numbers("[3]")
        self.assertEqual(actual, 3)

    def test_sum_numbers_WhenOneNumberInDictionary_ReturnsNumber(self):
        actual = sum_numbers("{\"a\":3}")
        self.assertEqual(actual, 3)

    def test_sum_numbers_WhenEmptyString_Returns0(self):
        actual = sum_numbers("")
        self.assertEqual(actual, 0)

    def test_sum_numbers_WhenNone_Returns0(self):
        actual = sum_numbers(None)
        self.assertEqual(actual, 0)

    def test_sum_numbers_WhenMultiDigitSingleNumberInList_ReturnsSum(self):
        actual = sum_numbers("[123]")
        self.assertEqual(actual, 123)

    def test_sum_numbers_WhenMultiDigitSingleNumberInDictionary_ReturnsSum(self):
        actual = sum_numbers("{\"a\":123}")
        self.assertEqual(actual, 123)

    def test_sum_numbers_WhenMultipleMultiDigitSingleNumbersInList_ReturnsSum(self):
        actual = sum_numbers("[1,42,32,55]")
        self.assertEqual(actual, 130)

    def test_sum_numbers_WhenMultipleMultiDigitSingleNumbersInDictionary_ReturnsSum(self):
        actual = sum_numbers("{\"a\":1,\"b\":42,\"c\":32,\"d\":55}")
        self.assertEqual(actual, 130)

    def test_sum_numbers_WhenNegativeNumberInList_ReturnsNumber(self):
        actual = sum_numbers("[-4]")
        self.assertEqual(actual, -4)

    def test_sum_numbers_WhenNegativeNumberInDictionary_ReturnsNumber(self):
        actual = sum_numbers("{\"a\":-4}")
        self.assertEqual(actual, -4)

    def test_sum_numbers_WhenNumbersAndTextInList_ReturnsSum(self):
        actual = sum_numbers("[\"text\",42,23,\"more text\",21]")
        self.assertEqual(actual, 86)

    def test_sum_numbers_WhenNumbersAndTextInDictionary_ReturnsSum(self):
        actual = sum_numbers("{\"a\":\"text\",\"b\":42,\"c\":23,\"d\":\"more text\",\"e\":21}")
        self.assertEqual(actual, 86)

    def test_sum_numbers_WhenListContainsList_IncludesSumOfChildList(self):
        actual = sum_numbers("[2,23,[55,10]]")
        self.assertEqual(actual, 90)

    def test_sum_numbers_WhenDictionaryContainsList_IncludesSumOfChildList(self):
        actual = sum_numbers("{\"a\":2,\"b\":23,\"c\":[55,10]}")
        self.assertEqual(actual, 90)

    def test_sum_numbers_WhenListContainsDictionary_IncludesSumOfChildDictionary(self):
        actual = sum_numbers("[2,23,{\"a\":55,\"b\":10}]")
        self.assertEqual(actual, 90)

    def test_sum_numbers_WhenDictionaryContainsDictionary_IncludesSumOfChildDictionary(self):
        actual = sum_numbers("{\"a\":2,\"b\":23,\"c\":[55,10]}")
        self.assertEqual(actual, 90)

    def test_sum_numbers_WhenDictionaryContainsValueOfRed_Returns0(self):
        actual = sum_numbers("{\"c\":\"red\",\"b\":2}", True)
        self.assertEqual(actual, 0)

    def test_sum_numbers_WhenListContainsDictionaryThatContainsValueOfRed_ExcludesDictionaryValuesSum(self):
        actual = sum_numbers("[1,{\"c\":\"red\",\"b\":2},3]", True)
        self.assertEqual(actual, 4)


def get_int_value(value):
    try:
        value = int(value)
    except ValueError:
        value = 0
    return value


def sum_numbers_in_value(value, ignore_red):
    sum_result = 0
    if isinstance(value, list):
        sum_result += sum_numbers_in_list(value, ignore_red)
    elif isinstance(value, dict):
        sum_result += sum_numbers_in_dictionary(value, ignore_red)
    else:
        sum_result += get_int_value(value)
    return sum_result


def sum_numbers_in_list(list_obj, ignore_red):
    sum_result = 0
    for value in list_obj:
        sum_result += sum_numbers_in_value(value, ignore_red)
    return sum_result


def sum_numbers_in_dictionary(dict_obj, ignore_red):
    sum_result = 0
    if ignore_red and "red" in dict_obj.values():
        return 0
    for value in dict_obj.values():
        sum_result += sum_numbers_in_value(value, ignore_red)
    return sum_result


def sum_numbers(text, ignore_red = False):
    if text is None:
        return 0
    if text == "":
        return 0

    json_obj = json.loads(text)
    return sum_numbers_in_value(json_obj, ignore_red)


def main():
    sum_of_numbers = 0
    sum_of_numbers_ignore_red = 0
    infile = open("input\\day_12.txt", "r")
    for line in infile:
        sum_of_numbers = sum_numbers(line)
        sum_of_numbers_ignore_red = sum_numbers(line, True)

    print("sum (including red): ", sum_of_numbers)
    print("sum (excluding red): ", sum_of_numbers_ignore_red)


if __name__ == '__main__':
    main()
