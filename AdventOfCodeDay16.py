import unittest
import re
from nose_parameterized import parameterized


class TestAdventOfCodeDay16(unittest.TestCase):
    def setUp(self):
        self.system_under_test = parse_sues(3, 7, 2, 3, 0, 0, 5, 3, 2, 1)

    def test_get_sue_number_WhenInvoked_ReturnsSueNumberFromLine(self):
        test_sue_line = r"Sue 11: cars: 9, children: 1, cats: 1"
        actual = self.system_under_test.get_sue_number(test_sue_line)
        self.assertEqual(actual, 11)

    def test_does_sue_match_WhenAllValuesMatch_ReturnsTrue(self):
        test_sue_line = r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"
        actual = self.system_under_test.does_sue_match(test_sue_line)
        self.assertTrue(actual)

    @parameterized.expand([
        ["Cats", r"Sue 11: cars: 2, children: 3, cats: 2, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Children", r"Sue 11: cars: 2, children: 6, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Samoyed", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 4, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Pomeranians", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 6, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Akitas", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 1, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Vizslas", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 3, goldfish: 5, trees: 3, perfumes: 1"],
        ["Goldfish", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 2, trees: 3, perfumes: 1"],
        ["Trees", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 9, perfumes: 1"],
        ["Cars", r"Sue 11: cars: 7, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 2, trees: 9, perfumes: 1"],
        ["Perfumes", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 2, trees: 9, perfumes: 0"]
    ])
    def test_does_sue_match_WhenItemDoesNotMatch_ReturnsFalse(self, name, test_sue_line):
        actual = self.system_under_test.does_sue_match(test_sue_line)
        self.assertFalse(actual)

    @parameterized.expand([
        ["Cats", r"Sue 11: cars: 2, children: 3, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Children", r"Sue 11: cars: 2, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Samoyeds", r"Sue 11: cars: 2, children: 3, cats: 7, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Cars", r"Sue 11: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Pomeranians", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Akitas", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, vizslas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Vizslas", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, goldfish: 5, trees: 3, perfumes: 1"],
        ["Goldfish", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, trees: 3, perfumes: 1"],
        ["Trees", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, perfumes: 1"],
        ["Perfumes", r"Sue 11: cars: 2, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3"]
    ])
    def test_does_sue_match_WhenItemNotPresent_ReturnsTrue(self, name, test_sue_line):
        actual = self.system_under_test.does_sue_match(test_sue_line)
        self.assertTrue(actual)


class parse_sues():
    def __init__(self, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
        self.children_re = self.create_re("children", children)
        self.cats_re = self.create_re("cats", cats)
        self.samoyeds_re = self.create_re("samoyeds", samoyeds)
        self.pomeranians_re = self.create_re("pomeranians", pomeranians)
        self.akitas_re = self.create_re("akitas", akitas)
        self.vizslas_re = self.create_re("vizslas", vizslas)
        self.goldfish_re = self.create_re("goldfish", goldfish)
        self.trees_re = self.create_re("trees", trees)
        self.cars_re = self.create_re("cars", cars)
        self.perfumes_re = self.create_re("perfumes", perfumes)

    def get_sue_number(self, sue_line):
        sue_line_segments = sue_line.split()
        sue_number_str = sue_line_segments[1]
        return int(sue_number_str.replace(":", ""))

    def create_re(self, text, count):
        return re.compile(r"^(({0}: {1})|((?!{0}).))*$".format(text, count))

    def does_sue_match(self, test_sue_line):
        return self.regular_expression_matches(self.children_re, test_sue_line) and \
               self.regular_expression_matches(self.cats_re, test_sue_line) and \
                self.regular_expression_matches(self.cars_re, test_sue_line) and \
                self.regular_expression_matches(self.samoyeds_re, test_sue_line) and \
                self.regular_expression_matches(self.pomeranians_re, test_sue_line) and \
                self.regular_expression_matches(self.akitas_re, test_sue_line) and \
                self.regular_expression_matches(self.vizslas_re, test_sue_line) and \
                self.regular_expression_matches(self.goldfish_re, test_sue_line) and \
                self.regular_expression_matches(self.trees_re, test_sue_line) and \
                self.regular_expression_matches(self.perfumes_re, test_sue_line)

    def regular_expression_matches(self, regular_expression, line):
        return regular_expression.match(line) != None