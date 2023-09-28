import time
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

    def test_get_present_count_WhenHouseNumber9AndPresentCount11_Returns143(self):
        actual = get_present_count(9, 11)
        self.assertEqual(143, actual)

    def test_get_present_count_WhenHouseNumber51PresentCount11HouseLimit50_Returns781(self):
        actual = get_present_count(51, 11, 50)
        self.assertEqual(781, actual)

    def test_get_present_count_WhenHouseNumber51PresentCount11NoHouseLimit_Returns1092(self):
        actual = get_present_count(50, 11)
        self.assertEqual(1023, actual)


def get_integer_divisors(number):
    divisors = []
    current_number = 1
    while current_number * current_number <= number:
        if number % current_number == 0:
            divisors.append(current_number)
            other_number = number / current_number
            if other_number != current_number:
                divisors.append(int(other_number))
        current_number += 1
    return divisors


def get_present_count(house_number, present_count_per_elf=10, house_limit=0):
    total_presents_count = 0
    elves = get_integer_divisors(house_number)
    for elf in elves:
        if (house_limit == 0) or (house_number / elf <= house_limit):
            total_presents_count += elf * present_count_per_elf
    return total_presents_count


def get_first_house_with_present_count_or_greater(target_present_count, present_count_per_elf=10, house_limit=0):
    current_house_number = 0
    current_present_count = 0
    while current_present_count < target_present_count:
        current_house_number += 1
        current_present_count = get_present_count(current_house_number, present_count_per_elf, house_limit)
    return current_house_number


def main():
    target_present_count = 29000000

    house_number = get_first_house_with_present_count_or_greater(target_present_count)
    print("House number: ", house_number)

    house_number = get_first_house_with_present_count_or_greater(target_present_count, 11, 50)
    print("House number (11 presents per elf, 50 house limit): ", house_number)


if __name__ == "__main__":
    main()
