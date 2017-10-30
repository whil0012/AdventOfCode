import unittest
import NamedPropertyItem
import itertools


class TestAdventOfCodeDay13(unittest.TestCase):
    def get_four_people_happiness_sets(self):
        person1_happiness_set1 = NamedPropertyItem.named_property_item(happiness=83, person1="Bob", person2="Alice")
        person1_happiness_set2 = NamedPropertyItem.named_property_item(happiness=-7, person1="Bob", person2="Carol")
        person1_happiness_set3 = NamedPropertyItem.named_property_item(happiness=-63, person1="Bob", person2="David")

        person2_happiness_set1 = NamedPropertyItem.named_property_item(happiness=54, person1="Alice", person2="Bob")
        person2_happiness_set2 = NamedPropertyItem.named_property_item(happiness=-79, person1="Alice", person2="Carol")
        person2_happiness_set3 = NamedPropertyItem.named_property_item(happiness=-2, person1="Alice", person2="David")

        person3_happiness_set1 = NamedPropertyItem.named_property_item(happiness=-62, person1="Carol", person2="Alice")
        person3_happiness_set2 = NamedPropertyItem.named_property_item(happiness=60, person1="Carol", person2="Bob")
        person3_happiness_set3 = NamedPropertyItem.named_property_item(happiness=55, person1="Carol", person2="David")

        person4_happiness_set1 = NamedPropertyItem.named_property_item(happiness=46, person1="David", person2="Alice")
        person4_happiness_set2 = NamedPropertyItem.named_property_item(happiness=-7, person1="David", person2="Bob")
        person4_happiness_set3 = NamedPropertyItem.named_property_item(happiness=41, person1="David", person2="Carol")

        return [person1_happiness_set1, person1_happiness_set2, person1_happiness_set3,
                          person2_happiness_set1, person2_happiness_set2, person2_happiness_set3,
                          person3_happiness_set1, person3_happiness_set2, person3_happiness_set3,
                          person4_happiness_set1, person4_happiness_set2, person4_happiness_set3]

    def test_get_happiness_set_WhenHappinessGained_ReturnsPositiveHappiness(self):
        actual = get_happiness_set("Alice would gain 54 happiness units by sitting next to Bob.")
        self.assertEqual(actual.happiness, 54)

    def test_get_happiness_set_WhenInvoked_ReturnsPerson1(self):
        actual = get_happiness_set("Alice would gain 54 happiness units by sitting next to Bob.")
        self.assertEqual(actual.person1, "Alice")

    def test_get_happiness_set_WhenInvoked_ReturnsPerson2(self):
        actual = get_happiness_set("Alice would gain 54 happiness units by sitting next to Bob.")
        self.assertEqual(actual.person2, "Bob")

    def test_get_happiness_set_WhenHappinessLost_ReturnsNegativeHappiness(self):
        actual = get_happiness_set("Alice would lose 79 happiness units by sitting next to Carol.")
        self.assertEqual(actual.happiness, -79)

    def test_get_happiness_set_WhenHappinessMultiplierCaseInconsisten_ReturnsNegativeHappiness(self):
        actual = get_happiness_set("Alice would lOsE 79 happiness units by sitting next to Carol.")
        self.assertEqual(actual.happiness, -79)

    def test_get_total_happines_for_pair_WhenTwoPeople_ReturnsTotalHappiness(self):
        person1_happiness_set = NamedPropertyItem.named_property_item(happiness=42, person1="Alice", person2="Bob")
        person2_happiness_set = NamedPropertyItem.named_property_item(happiness=23, person1="Bob", person2="Alice")
        happiness_sets = [person1_happiness_set, person2_happiness_set]
        actual = get_total_happiness_for_pair(happiness_sets, "Alice", "Bob")
        self.assertEqual(actual, 65)

    def test_get_total_happines_for_pair_WhenFourPeople_ReturnsTotalHappiness(self):
        happiness_sets = self.get_four_people_happiness_sets()
        actual = get_total_happiness_for_pair(happiness_sets, "Carol", "Bob")
        self.assertEqual(actual, 53)

    def test_get_total_happines_WhenInvoked_ReturnsTotalHappiness(self):
        happiness_sets = self.get_four_people_happiness_sets()
        actual = get_total_happiness(happiness_sets, ["David", "Bob", "Alice", "Carol"])
        self.assertEqual(actual, 22)

    def test_get_unique_persons_WhenFourPeople_ReturnsFourPeople(self):
        happiness_sets = self.get_four_people_happiness_sets()
        actual = get_unique_persons(happiness_sets)
        expected = ["Bob", "Alice", "Carol", "David"]
        self.assertCountEqual(actual, expected)

    # def test_get_maximum_happiness_WhenInvoked_ReturnsMaximumHappiness(self):
    #     happiness_sets = self.get_four_people_happiness_sets()
    #     actual = get_maximum_happiness(happiness_sets)
    #     expected = ["Alice", "Bob", "Carol", "David"]
    #     self.assertListEqual(actual, expected)



description_index_happiness_value = 3
description_index_person1 = 0
description_index_person2 = 10
description_index_happiness_multiplier = 2
description_text_lose = "lose"


def get_unique_persons(happiness_sets):
    unique_persons = []
    [unique_persons.append(x.person1) for x in happiness_sets if x.person1 not in unique_persons]
    return unique_persons


def is_person(person_test_1, person_test_2):
    return person_test_1.casefold() == person_test_2.casefold()


def is_person1(happiness_set, person):
    return is_person(happiness_set.person1, person)


def is_person2(happiness_set, person):
    return is_person(happiness_set.person2, person)


def is_relevant_happiness_set(happiness_set, first_person, second_person):
    return (is_person1(happiness_set, first_person) and is_person2(happiness_set, second_person)) or\
           (is_person1(happiness_set, second_person) and is_person2(happiness_set, first_person))


def get_total_happiness_for_pair(happiness_sets, first_person, second_person):
    relevant_happiness_values = [x.happiness for x in happiness_sets
                                 if is_relevant_happiness_set(x, first_person, second_person)]
    return sum(relevant_happiness_values)


def get_happiness_multiplier(happiness_description_multiplier):
    if happiness_description_multiplier.casefold() == description_text_lose.casefold():
        return -1
    else:
        return 1


def get_happiness_set(happiness_description):
    description_segments = [x.strip() for x in happiness_description.split(" ")]
    happiness_multiplier = get_happiness_multiplier(description_segments[description_index_happiness_multiplier])
    happiness_value = int(description_segments[description_index_happiness_value]) * happiness_multiplier
    person1 = description_segments[description_index_person1]
    person2 = description_segments[description_index_person2].replace(".", "")
    return get_happiness_set_item(happiness_value, person1, person2)


def get_happiness_set_item(happiness_value, person1, person2):
    return NamedPropertyItem.named_property_item(happiness=happiness_value,
                                                 person1=person1,
                                                 person2=person2)


def get_total_happiness(happiness_sets, seating_arrangement):
    total_happiness = 0
    for i in range(0, len(seating_arrangement)):
        person1 = seating_arrangement[i]
        if i < len(seating_arrangement) - 1:
            person2 = seating_arrangement[i + 1]
        else:
            person2 = seating_arrangement[0]
        total_happiness += get_total_happiness_for_pair(happiness_sets, person1, person2)
    return total_happiness


def get_minimum_happiness(happiness_sets, seating_arrangement):
    minimum_happiness = get_total_happiness_for_pair(happiness_sets, seating_arrangement[0], seating_arrangement[1])
    for i in range(0, len(seating_arrangement)):
        person1 = seating_arrangement[i]
        if i < len(seating_arrangement) - 1:
            person2 = seating_arrangement[i + 1]
        else:
            person2 = seating_arrangement[0]
        total_happiness = get_total_happiness_for_pair(happiness_sets, person1, person2)
        if total_happiness < minimum_happiness:
            minimum_happiness = total_happiness
    return minimum_happiness


def get_unique_persons_combinations(happiness_sets):
    unique_persons = get_unique_persons(happiness_sets)
    return itertools.permutations(unique_persons)


def get_happiness_values_from_unique_combinations(happiness_sets, unique_persons_combinations):
    happiness_values = []
    for unique_persons_combination in unique_persons_combinations:
        total_happiness = get_total_happiness(happiness_sets, unique_persons_combination)
        happiness_values.append(NamedPropertyItem.named_property_item(total_happiness=total_happiness, seating_arrangement=list(unique_persons_combination)))
    return happiness_values


def get_happiness_values(happiness_sets):
    unique_persons_combinations = get_unique_persons_combinations(happiness_sets)
    return get_happiness_values_from_unique_combinations(happiness_sets, unique_persons_combinations)


def get_maximum_happiness(happiness_sets):
    happiness_values = get_happiness_values(happiness_sets)
    max_happiness_value = happiness_values[0]
    for happiness_value in happiness_values:
        if happiness_value.total_happiness > max_happiness_value.total_happiness:
            max_happiness_value = happiness_value
    return max_happiness_value


def get_happiness_sets_with_me(happiness_sets):
    happiness_sets_result = happiness_sets
    unique_persons = get_unique_persons(happiness_sets)
    happiness_sets_with_me_as_person1 = [get_happiness_set_item(0, "Levi", x) for x in unique_persons]
    happiness_sets_with_me_as_person2 = [get_happiness_set_item(0, x, "Levi") for x in unique_persons]
    for happiness_set in happiness_sets_with_me_as_person1:
        happiness_sets_result.append(happiness_set)
    for happiness_set in happiness_sets_with_me_as_person2:
        happiness_sets_result.append(happiness_set)
    return happiness_sets_result


def main():
    with open("input/day_13.txt", "r") as input_file:
        happiness_sets = [get_happiness_set(x) for x in input_file]
    max_happiness = get_maximum_happiness(happiness_sets)
    print(max_happiness.seating_arrangement)
    print(max_happiness.total_happiness)

    happiness = get_minimum_happiness(happiness_sets, max_happiness.seating_arrangement)
    print(happiness)
    # happiness_sets_with_me = get_happiness_sets_with_me(happiness_sets)
    # max_happiness = get_maximum_happiness(happiness_sets_with_me)
    # print(max_happiness.seating_arrangement)
    # print(max_happiness.total_happiness)



if __name__ == "__main__":
    main()
