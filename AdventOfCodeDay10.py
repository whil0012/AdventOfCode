import unittest
import time


class TestAdventOfCodeDay10(unittest.TestCase):
    def testLookSay_When1_Returns11(self):
        next_value = look_say("1")
        self.assertEqual(next_value, "11")

    def testLookSay_When11_Returns21(self):
        next_value = look_say("11")
        self.assertEqual(next_value, "21")

    def testLookSay_When111221_Returns312211(self):
        next_value = look_say("111221")
        self.assertEqual(next_value, "312211")


def look_say(value):
    last_digit = value[0]
    current_digit_count = 0
    result = ""
    for digit in value:
        if digit != last_digit:
            result += str(current_digit_count) + last_digit
            current_digit_count = 1
        else:
            current_digit_count += 1
        last_digit = digit

    result += str(current_digit_count) + last_digit
    return result


def main():
    next_value = "3113322113"
    for _i in range(40):
        next_value = look_say(next_value)
    print("length: ", len(next_value))
    for _i in range(10):
        next_value = look_say(next_value)
    print("length: ", len(next_value))


if __name__ == '__main__':
    main()