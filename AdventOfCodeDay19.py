import unittest
import os
import NamedPropertyItem


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

    def test_get_transitions_count_WhenHOH_Returns3(self):
        transitions = [NamedPropertyItem.named_property_item(item = 'H', replacement = 'HO'),
                    NamedPropertyItem.named_property_item(item='H', replacement='OH'),
                    NamedPropertyItem.named_property_item(item='O', replacement='HH'),
                    NamedPropertyItem.named_property_item(item='e', replacement='H'),
                    NamedPropertyItem.named_property_item(item='e', replacement='O')]
        actual = get_transitions_count(transitions, 'HOH')
        self.assertEqual(actual, 3)

    def test_get_transitions_count_WhenHOHOHO_Returns6(self):
        transitions = [NamedPropertyItem.named_property_item(item = 'H', replacement = 'HO'),
                    NamedPropertyItem.named_property_item(item='H', replacement='OH'),
                    NamedPropertyItem.named_property_item(item='O', replacement='HH'),
                    NamedPropertyItem.named_property_item(item='e', replacement='H'),
                    NamedPropertyItem.named_property_item(item='e', replacement='O')]
        actual = get_transitions_count(transitions, 'HOHOHO')
        self.assertEqual(actual, 6)


line_segment_index_item_to_replace = 0
line_segment_index_replacement = 2


def get_transitions_count(transitions, desired_molecule):
    non_e_transitions = get_non_e_transitions(transitions)
    count = make_reverse_transitions(non_e_transitions, desired_molecule)
    return count + 1


def make_reverse_transitions(transitions, desired_molecule):
    total_count = 0
    current_molecule = desired_molecule
    transitions_sorted = sorted(transitions, key=lambda x: len(x.replacement), reverse=True)
    attempt_more_transitions = True
    while attempt_more_transitions:
        transitions_loop_count = 0
        for transition in transitions_sorted:
            transitions_result = make_reverse_transitions_for_item(transition, current_molecule)
            transitions_loop_count += transitions_result.count
            current_molecule = transitions_result.molecule
        total_count += transitions_loop_count
        attempt_more_transitions = transitions_loop_count > 0
    return total_count


def make_reverse_transitions_for_item(transition, molecule):
    return make_reverse_transitions_for_item_replacement(transition.item, transition.replacement, molecule)


def make_reverse_transitions_for_item_replacement(item, replacement, molecule):
    transitions_count = 0
    current_molecule = molecule
    while replacement in current_molecule:
        current_molecule = current_molecule.replace(replacement, item, 1)
        transitions_count += 1
    return NamedPropertyItem.named_property_item(molecule = current_molecule, count = transitions_count)


def get_non_e_transitions(transitions):
    return [x for x in transitions if x.item != 'e']


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


def get_transition_named_property_item(line):
    line_segments = line.strip().split(' ')
    item_to_replace = line_segments[line_segment_index_item_to_replace]
    replacement = line_segments[line_segment_index_replacement]
    return NamedPropertyItem.named_property_item(item = item_to_replace, replacement = replacement)


def get_exploded_transitions_list(lines):
    return [get_transition_named_property_item(x) for x in lines]


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
        input_file.seek(0)
        transitions_list = get_exploded_transitions_list(input_file)
    distinct_molecules = get_distinct_molecules(transitions, formula)
    print("number of distinct molecules: ", len(distinct_molecules))
    transitions_count = get_transitions_count(transitions_list, formula)
    print("number of transitions: ", transitions_count)


if __name__ == "__main__":
    main()