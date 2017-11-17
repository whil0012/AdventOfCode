import unittest
from enum import Enum
import os


class TestAdventOfCodeDay18(unittest.TestCase):
    def test_get_light_states_WhenInvoked_ReturnsLightStates(self):
        light_states = get_light_states_from_lines(['#.#', '###', '...'])
        self.assertListEqual(light_states[0], [Light_State.On, Light_State.Off, Light_State.On])
        self.assertListEqual(light_states[1], [Light_State.On, Light_State.On, Light_State.On])
        self.assertListEqual(light_states[2], [Light_State.Off, Light_State.Off, Light_State.Off])

    def test_update_lights_When0NeighborLightsOn_TurnsLightOff(self):
        light_states = get_light_states_from_lines(['...', '.#.', '...'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.Off)

    def test_update_lights_When1NeighborLightsOn_TurnsLightOff(self):
        light_states = get_light_states_from_lines(['.#.', '.#.', '...'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.Off)

    def test_update_lights_WhenOnAnd2NeighborLightsOn_TurnsLightOn(self):
        light_states = get_light_states_from_lines(['...', '###', '...'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.On)

    def test_update_lights_WhenOnAnd3NeighborLightsOn_TurnsLightOn(self):
        light_states = get_light_states_from_lines(['..#', '###', '...'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.On)

    def test_update_lights_WhenOnAnd4NeighborLightsOn_TurnsLightOff(self):
        light_states = get_light_states_from_lines(['..#', '###', '.#.'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.Off)

    def test_update_lights_WhenOffAnd3NeighborLightsOn_TurnsLightOn(self):
        light_states = get_light_states_from_lines(['..#', '#.#', '...'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.On)

    def test_update_lights_WhenOffAnd4NeighborLightsOn_TurnsLightOff(self):
        light_states = get_light_states_from_lines(['..#', '#.#', '#..'])
        light_states_next_step = update_lights(light_states)
        self.assertEquals(light_states_next_step[1][1], Light_State.Off)

    def test_count_lights_on_When4LightsOn_Returns4(self):
        light_states = get_light_states_from_lines(['..#', '#.#', '#..'])
        actual = count_lights_on(light_states)
        self.assertEquals(actual, 4)

    def test_update_lights_WhenStuckLights_LeaversCornersOn(self):
        light_states = get_light_states_from_lines(['#.#', '#.#', '#.#'])
        light_states_next_step = update_lights(light_states, True)
        self.assertEquals(light_states_next_step[0][0], Light_State.On)
        self.assertEquals(light_states_next_step[0][2], Light_State.On)
        self.assertEquals(light_states_next_step[2][0], Light_State.On)
        self.assertEquals(light_states_next_step[2][2], Light_State.On)



class Light_State(Enum):
    Off = 0
    On = 1


def count_lights_on(light_states):
    return sum([x.count(Light_State.On) for x in light_states])


def update_lights(light_states, lights_are_stuck = False):
    new_light_states =  [[x for x in row] for row in light_states]
    for i in range(0, len(light_states)):
        for j in range(0, len(light_states[i])):
            if lights_are_stuck and \
                ((i == 0 and j == 0) or (i == 0 and j == len(light_states[i]) - 1) or \
                 (i == len(light_states) - 1 and j == 0) or (i == len(light_states) - 1 and j == len(light_states[i]) - 1)):
                new_light_states[i][j] = Light_State.On
                continue
            neighbor_count = count_on_neighbors(i, j, light_states)
            if light_states[i][j] == Light_State.On:
                new_light_states[i][j] = Light_State.On if (neighbor_count == 2 or neighbor_count == 3) else Light_State.Off
            else:
                new_light_states[i][j] = Light_State.On if neighbor_count == 3 else Light_State.Off
    return new_light_states


def is_in_range(row, column, light_states):
    return row >= 0 and row < len(light_states) and \
            column >= 0 and column < len(light_states[row])


def count_on_neighbors(row, column, light_states):
    count = 0
    for row_adjust in range(-1, 2):
        for column_adjust in range(-1, 2):
            neighbor_row = row + row_adjust
            neighbor_column = column + column_adjust
            if (neighbor_row != row or neighbor_column != column) and is_in_range(neighbor_row, neighbor_column, light_states):
                count += 1 if light_states[neighbor_row][neighbor_column] == Light_State.On else 0
    return count


def get_light_states_from_line(line):
    return [Light_State.On if x == '#' else Light_State.Off for x in line]


def get_light_states_from_lines(lines):
    return [get_light_states_from_line(x) for x in lines]


def main():
    with open(os.path.join("input", "day_18.txt"), "r") as input_file:
        light_states = [get_light_states_from_line(x.strip()) for x in input_file]
    for step in range(0, 100):
        # light_states = update_lights(light_states)
        light_states = update_lights(light_states, True)
    count = count_lights_on(light_states)
    print("count of lights on: ", count)


if __name__ == "__main__":
    main()