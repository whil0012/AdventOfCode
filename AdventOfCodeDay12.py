import unittest


class TestAdventOfCodeDay12(unittest.TestCase):
    def testSumNumbers_WhenNoNumbers_Returns0(self):
        actual = sumNumbers("this has no numbers")
        self.assertEqual(actual, 0)

    def testSumNumbers_WhenOneNumber_ReturnsNumber(self):
        actual = sumNumbers("this has a number 3")
        self.assertEqual(actual, 3)

    def testSumNumbers_WhenEmptyString_Returns0(self):
        actual = sumNumbers("")
        self.assertEqual(actual, 0)

    def testSumNumbers_WhenNone_Returns0(self):
        actual = sumNumbers(None)
        self.assertEqual(actual, 0)

    def testSumNumbers_WhenNumbersAtBeginningAndEnd_ReturnsSum(self):
        actual = sumNumbers("4 text 5 more text 2")
        self.assertEqual(actual, 11)

    def testSumNumbers_WhenMultiDigitSingleNumber_ReturnsSum(self):
        actual = sumNumbers("text 123")
        self.assertEqual(actual, 123)

    def testSumNumbers_WhenMultipleMultiDigitSingleNumbers_ReturnsSum(self):
        actual = sumNumbers("1 some text 42 32 more text 55")
        self.assertEqual(actual, 130)

    def testSumNumbers_WhenNegativeNumber_ReturnsNumber(self):
        actual = sumNumbers("-4")
        self.assertEqual(actual, -4)


def get_int_value(text):
    value = 0
    try:
        value = int(text)
    except:
        value = 0
    return value


def sumNumbers(text):
    if text is None:
        return 0

    found_number_string = ""
    numbers_sum = 0

    for character in text:
        if character.isnumeric() or character == '-':
            found_number_string += character
        else:
            numbers_sum += get_int_value(found_number_string)
            found_number_string = ""
    numbers_sum += get_int_value(found_number_string)
    return numbers_sum


def main():
    sum_of_numbers = 0
    infile = open("input\\day_12.txt", "r")
    for line in infile:
        sum_of_numbers += sumNumbers(line)

    print("sum: ", sum_of_numbers)


if __name__ == '__main__':
    main()
