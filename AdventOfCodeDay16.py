import unittest
import re


class TestAdventOfCodeDay16(unittest.TestCase):
    def setUp(self):
        self.system_under_test = parse_sues(3, 7, 2, 3, 0, 0, 5, 3, 2, 1)

    def test_get_sue_number_WhenInvoked_ReturnsSueNumberFromLine(self):
        test_sue_line = r"Sue 11: cars: 9, children: 1, cats: 1"
        actual = self.system_under_test.get_sue_number(test_sue_line)
        self.assertEqual(actual, 11)

    def test_does_sue_match_WhenAllValuesMatch_ReturnsTrue(self):
        test_sue_line = r"Sue 11: cars: 9, children: 1, cats: 1" # TODO : Update this line
        actual = self.system_under_test.does_sue_match(test_sue_line)
        self.assertTrue(actual)


class parse_sues():
    def __init__(self, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
        self.set_regular_expression()
# children_re = re.compile(r"^((children: 3)|((?!children).))*$")
# r"{}: {}".format(cats_desc, cats_count)

    def get_sue_number(self, sue_line):
        sue_line_segments = sue_line.split()
        sue_number_str = sue_line_segments[1]
        return int(sue_number_str.replace(":", ""))

    def set_regular_expression(self):
        pass

    def does_sue_match(self, test_sue_line):
        return False