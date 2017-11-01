import unittest
import itertools


class TestAdventOfCodeDay15(unittest.TestCase):
    def test_get_all_combinations_for_100_WhenInvoked_ReturnsOnlyCombinationsThatSumTo100(self):
        actual = get_all_combinations_for_100()
        for combination in actual:
            combination_sum = sum(combination)
            self.assertEqual(combination_sum , 100, combination)

    def test_get_all_combinatins_for_100_WhenInvoked_ReturnsOnlyNumbersBetween1and97(self):
        # 97 is the maximum number that can be in a combination with 3 other numbers greater than 0, i.e. [1, 1, 1, 97]
        actual = get_all_combinations_for_100()
        for combination in actual:
            for number in combination:
                self.assertTrue(number >= 1, "number: " + str(number) + "; combination: " + str(combination))
                self.assertTrue(number <= 97, "number: " + str(number) + "; combination: " + str(combination))



def get_all_combinations_for_100():
    for first_number in range(1, 98):
        for second_number in range(1, 99 - first_number):
            for third_number in range(1, 100 - (first_number + second_number)):
                yield [first_number, second_number, third_number, 100 - (first_number + second_number + third_number)]
