import unittest
import os


class TestAdventOfCodeDay19(unittest.TestCase):
    def test_get_distinct_molecules_WhenThreeTransitionsAndHOHStart_Returns4DistinctMolecules(self):
        transitions = {'H' : ['HO', 'OH'], 'O': ['HH']}
        actual = get_distinct_molecules(transitions, 'HOH')
        expected = set(['HOOH', 'HOHO', 'OHOH', 'HHHH'])
        self.assertSetEqual(actual, expected)

    def test_get_transitions_from_lines_WhenThreeLinesAndTwoItemsWithSameStart_ReturnsTwoItemsWithLists(self):
        test_lines = ['Al => ThF', 'Al => ThRnFAr', 'B => BCa']
        actual = get_transitions_from_lines(test_lines)
        expected = {'Al': ['ThF', 'ThRnFAr'], 'B': ['BCa']}
        self.assertDictEqual(actual, expected)


line_segment_index_item_to_replace = 0
line_segment_index_replacement = 2


def add_transition_from_line(line, transitions):
    line_segments = line.strip().split(' ')
    item_to_replace = line_segments[line_segment_index_item_to_replace]
    replacement = line_segments[line_segment_index_replacement]
    if item_to_replace not in transitions:
        transitions[item_to_replace] = []
    transitions[item_to_replace].append(replacement)


def add_transitions_from_lines(lines, transitions):
    for line in lines:
        add_transition_from_line(line, transitions)


def get_transitions_from_lines(lines):
    result = {}
    add_transitions_from_lines(lines, result)
    return result


def add_distinct_molecules_for_replacement_item(starting_molecule, item_to_replace, replacement_item,
                                                distinct_molecules):
    occurrence = starting_molecule.find(item_to_replace, 0)
    while occurrence >= 0:
        new_molecule = starting_molecule[:occurrence] + replacement_item + starting_molecule[occurrence + len(item_to_replace):]
        distinct_molecules.add(new_molecule.strip())
        occurrence = starting_molecule.find(item_to_replace, occurrence + 1)


def add_distinct_molecules_for_replacement_list(starting_molecule, item_to_replace, replacement_list,
                                                distinct_molecules):
    for replacement_item in replacement_list:
        add_distinct_molecules_for_replacement_item(starting_molecule, item_to_replace, replacement_item, distinct_molecules)


def add_distinct_molecules(transitions, starting_molecule, distinct_molecules):
    for item_to_replace, replacement_list in transitions.items():
        add_distinct_molecules_for_replacement_list(starting_molecule, item_to_replace, replacement_list, distinct_molecules)


def get_distinct_molecules(transitions, starting_molecule):
    result = set()
    add_distinct_molecules(transitions, starting_molecule, result)
    return result


formula = r'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'


def main():
    file_path = os.path.join("input", "day_19_transitions.txt")
    with open(file_path, "r") as input_file:
        transitions = get_transitions_from_lines(input_file)
    distinct_molecules = get_distinct_molecules(transitions, formula)
    print("number of distinct molecules: ", len(distinct_molecules))


if __name__ == "__main__":
    main()