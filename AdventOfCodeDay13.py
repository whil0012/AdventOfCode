import unittest
import NamedPropertyItem


class TestAdventOfCodeDay13(unittest.TestCase):
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
        person1_happiness_set1 = NamedPropertyItem.named_property_item(happiness=54, person1="Alice", person2="Bob")
        person1_happiness_set2 = NamedPropertyItem.named_property_item(happiness=-79, person1="Alice", person2="Carol")
        person1_happiness_set3 = NamedPropertyItem.named_property_item(happiness=-2, person1="Alice", person2="David")

        person2_happiness_set1 = NamedPropertyItem.named_property_item(happiness=83, person1="Bob", person2="Alice")
        person2_happiness_set2 = NamedPropertyItem.named_property_item(happiness=-7, person1="Bob", person2="Carol")
        person2_happiness_set3 = NamedPropertyItem.named_property_item(happiness=-63, person1="Bob", person2="David")

        person3_happiness_set1 = NamedPropertyItem.named_property_item(happiness=-62, person1="Carol", person2="Alice")
        person3_happiness_set2 = NamedPropertyItem.named_property_item(happiness=60, person1="Carol", person2="Bob")
        person3_happiness_set3 = NamedPropertyItem.named_property_item(happiness=55, person1="Carol", person2="David")

        person4_happiness_set1 = NamedPropertyItem.named_property_item(happiness=46, person1="David", person2="Alice")
        person4_happiness_set2 = NamedPropertyItem.named_property_item(happiness=-7, person1="David", person2="Bob")
        person4_happiness_set3 = NamedPropertyItem.named_property_item(happiness=41, person1="David", person2="Carol")

        happiness_sets = [person1_happiness_set1, person1_happiness_set2, person1_happiness_set3,
                          person2_happiness_set1, person2_happiness_set2, person2_happiness_set3,
                          person3_happiness_set1, person3_happiness_set2, person3_happiness_set3,
                          person4_happiness_set1, person4_happiness_set2, person4_happiness_set3]
        actual = get_total_happiness_for_pair(happiness_sets, "Carol", "Bob")
        self.assertEqual(actual, 53)


description_index_happiness_value = 3
description_index_person1 = 0
description_index_person2 = 10
description_index_happiness_multiplier = 2
description_text_lose = "lose"


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
    return NamedPropertyItem.named_property_item(happiness=happiness_value,
                                                 person1=person1,
                                                 person2=person2)