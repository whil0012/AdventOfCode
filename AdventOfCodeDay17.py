import unittest
import itertools
import os


class TestAdventOfCodeDay17(unittest.TestCase):
    def test_get_number_of_combinations_WhenInvoked_ReturnsNumberOfCombinations(self):
        containers = [20, 15, 10, 5, 5]
        actual = get_number_of_combinations(containers, 25)
        self.assertEquals(actual, 4)


def get_number_of_matches(combinations_of_containers, total_volume):
    count = 0
    for container_combination in combinations_of_containers:
        combination_volume = sum(container_combination)
        if combination_volume == total_volume:
            count += 1
    return count


def get_number_of_combinations(containers, total_volume):
    count = 0
    for i in range(1, len(containers) + 1):
        combinations_of_containers = itertools.combinations(containers, i)
        count += get_number_of_matches(combinations_of_containers, total_volume)
    return count


def main():
    with open(os.path.join("input", "day_17.txt"), "r") as input_file:
        containers = [int(x) for x in input_file]
    number_of_combinations = get_number_of_combinations(containers, 150)
    print("number of conbinations: ", number_of_combinations)


if __name__ == "__main__":
    main()