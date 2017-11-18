import unittest
import os


class TestAdventOfCodeDay19(unittest.TestCase):
    def test_get_distinct_molecules_WhenThreeTransitionsAndHOHStart_Returns4DistinctMolecules(self):
        transitions = {'H' : ['HO', 'OH'], 'O': ['HH']}
        actual = get_distinct_molecules(transitions, 'HOH')
        expected = set(['HOOH', 'HOHO', 'OHOH', 'HHHH'])
        self.assertSetEqual(actual, expected)


def get_distinct_molecules(transitions, starting_molecule):
    result = set()
    # occurrence = starting_molecule.find(item_to_replace, 0)
    # new_molecule = starting_molecule[:occurrence] + item_replacement + test_string[occurence + len(item_to_replace):]
    # occurrence = starting_molecule.find(item_to_replace, occurrence + 1)
    # ... until occurrence == -1 || while occurrence >= 0, etc
    # is there a do until? or do { } while?
    return result
