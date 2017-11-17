import unittest
import os


class TestAdventOfCodeDay19(unittest.TestCase):
    def test_get_distinct_molecules_WhenThreeTransitionsAndHOHStart_Returns4DistinctMolecules(self):
        transitions = {'H' : ['HO', 'OH'], 'O': ['HH']}
        actual = get_distinct_molecules(transitions, 'HOH')
        expected = set(['HOOH', 'HOHO', 'OHOH', 'HHHH'])
        self.assertSetEqual(actual, expected)


def get_distinct_molecules(transitions, param):
    return set()
