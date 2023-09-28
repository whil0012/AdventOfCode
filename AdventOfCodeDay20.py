import unittest

class TestAdventOfCodeDay20(unittest.TestCase):
    def test_get_present_count_WhenHouseNumber0_Returns0(self):
        actual = get_present_count(0)
        self.assertEqual(0, actual)

    def test_get_present_count_WhenHouseNumber1_Returns10(self):
        actual = get_present_count(1)
        self.assertEqual(10, actual)

    def test_get_present_count_WhenHouseNumber2_Returns30(self):
        actual = get_present_count(2)
        self.assertEqual(30, actual)

    def test_get_present_count_WhenHouseNumber3_Returns30(self):
        actual = get_present_count(3)
        self.assertEqual(40, actual)

    def test_get_present_count_WhenHouseNumber9_Returns130(self):
        actual = get_present_count(9)
        self.assertEqual(130, actual)


def get_integer_divisors(number):
    divisors = []
    current_number = 1
    while current_number * current_number <= number:
        if number % current_number == 0:
            divisors.append(current_number)
            other_number = number / current_number
            if other_number != current_number:
                divisors.append(other_number)
        current_number += 1
    return divisors


def get_present_count(house_number):
    total_presents_count = 0
    elves = get_integer_divisors(house_number)
    for elf in elves:
        total_presents_count += elf * 10
    return total_presents_count


def main():
    target_present_count = 29000000
    current_house_number = 0
    current_present_count = 0
    while current_present_count < target_present_count:
        current_house_number += 1
        current_present_count = get_present_count(current_house_number)
    print("House number: ", current_house_number)
    print("Present count: ", current_present_count)


if __name__ == "__main__":
    main()
