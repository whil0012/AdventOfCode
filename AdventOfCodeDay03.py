import unittest


class TestAdventOfCodeDay03(unittest.TestCase):
    def testCountHouseVisits_WithNone_ReturnsOne(self):
        actual = count_house_visits(None)
        self.assertEqual(actual, 1)

    def testCountHouseVisits_WithEmptyString_ReturnsOne(self):
        actual = count_house_visits("")
        self.assertEqual(actual, 1)

    def testCountHouseVisits_OneDirectionCommand_ReturnsTwo(self):
        actual = count_house_visits(">")
        self.assertEqual(actual, 2)

    def testCountHouseVisits_FourDirectionCommandsOneRepeat_ReturnsFour(self):
        actual = count_house_visits("^>v<")
        self.assertEqual(actual, 4)

    def testCountHouseVisits_TenCommandsTwoRepeated_ReturnsTwo(self):
        actual = count_house_visits("^v^v^v^v^v")
        self.assertEqual(actual, 2)

    def testCountHouseVisitsWithRoboSanta_WithNone_ReturnsOne(self):
        actual = count_house_visits_with_robo_santa(None)
        self.assertEqual(actual, 1)

    def testCountHouseVisitsWithRoboSanta_WithEmptyString_ReturnsOne(self):
        actual = count_house_visits_with_robo_santa("")
        self.assertEqual(actual, 1)

    def testCountHouseVisitsWithRoboSanta_WithTwoDifferentCommands_ReturnsThree(self):
        actual = count_house_visits_with_robo_santa("^v")
        self.assertEqual(actual, 3)

    def testCountHouseVisitsWithRoboSanta_WithFourCommandsOneRepeatedDest_ReturnsThree(self):
        actual = count_house_visits_with_robo_santa("^>v<")
        self.assertEqual(actual, 3)

    def testCountHouseVisitsWithRoboSanta_WithTenCommandsNoRepeatDest_ReturnsEleven(self):
        actual = count_house_visits_with_robo_santa("^v^v^v^v^v")
        self.assertEqual(actual, 11)

    def testCountHouseVisitsWithRoboSanta_WithRepeatedDest_ReturnsDistinctHouses(self):
        actual = count_house_visits_with_robo_santa("^>>^^v")
        self.assertEqual(actual, 5)

    def testCountHouseVisits_WithInvalidCharacters_ReturnsDistinctHouses(self):
        actual = count_house_visits("^>Dv<")
        self.assertEqual(actual, 4)


def add_house_visits(visited_houses, direction_commands):
    current_x_position = 0
    current_y_position = 0
    visited_houses.add((current_x_position, current_y_position))
    if direction_commands is None:
        return
    for direction in direction_commands:
        if direction == "^":
            current_y_position += 1
        elif direction == "v":
            current_y_position -= 1
        elif direction == "<":
            current_x_position -= 1
        elif direction == ">":
            current_x_position += 1
        visited_houses.add((current_x_position, current_y_position))


def count_house_visits(direction_commands):
    visited_house_set = set()
    add_house_visits(visited_house_set, direction_commands)
    return len(visited_house_set)


def count_house_visits_with_robo_santa(direction_commands):
    santa_direction_commands = direction_commands[::2] if direction_commands is not None else None
    robo_santa_direction_commands = direction_commands[1::2] if direction_commands is not None else None
    visited_house_set = set()
    add_house_visits(visited_house_set, santa_direction_commands)
    add_house_visits(visited_house_set, robo_santa_direction_commands)
    return len(visited_house_set)


def main():
    number_of_houses = 0
    number_of_houses_with_robo_santa = 0
    with open("input/day_03.txt", "r") as inputFile:
        input_text = inputFile.read()
        number_of_houses += count_house_visits(input_text)
        number_of_houses_with_robo_santa += count_house_visits_with_robo_santa(input_text)
    print("number of houses: ", number_of_houses)
    print("number of houses with robo santa: ", number_of_houses_with_robo_santa)


if __name__ == "__main__":
    main()