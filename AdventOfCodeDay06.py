import unittest
from enum import Enum


class TestAdventOfCodeDay06(unittest.TestCase):
    def setUp(self):
        self.AdventOfCodeDay06Inst = AdventOfCodeDay06OnOff()

    def testProcessCommand_TurnOnOneLight_TurnsOnLights(self):
        self.AdventOfCodeDay06Inst.process_command("turn on 0,0 through 0,0")
        self.assertEqual(self.AdventOfCodeDay06Inst.Light_Grid[0][0], True, "Light_Grid[0][0]")

    def testProcessCommand_TurnOnNineLights_TurnsOnLights(self):
        self.AdventOfCodeDay06Inst.process_command("turn on 2,3 through 5,7")
        self.__assert_lights_values((2, 3), (5, 7), True)

    def testProcessCommand_TurnOffFourLights_TurnsOffLights(self):
        self.AdventOfCodeDay06Inst.Light_Grid[1][0] = True
        self.AdventOfCodeDay06Inst.Light_Grid[1][1] = True
        self.AdventOfCodeDay06Inst.Light_Grid[2][0] = True
        self.AdventOfCodeDay06Inst.Light_Grid[2][1] = True
        self.AdventOfCodeDay06Inst.process_command("turn off 1,0 through 2,1")
        self.__assert_lights_values((1, 0), (2, 1), False)

    def testProcessCommand_TurnOnAtEnd_TurnsOnLights(self):
        self.AdventOfCodeDay06Inst.process_command("turn on 995,997 through 999,999")
        self.__assert_lights_values((995, 997), (999, 999), True)

    def testProcessCommand_ToggleFourLights_TogglesLights(self):
        self.AdventOfCodeDay06Inst.Light_Grid[1][0] = True
        self.AdventOfCodeDay06Inst.Light_Grid[1][1] = False
        self.AdventOfCodeDay06Inst.Light_Grid[2][0] = True
        self.AdventOfCodeDay06Inst.Light_Grid[2][1] = False
        self.AdventOfCodeDay06Inst.process_command("toggle 1,0 through 2,1")
        self.assertEqual(self.AdventOfCodeDay06Inst.Light_Grid[1][0], False, "Light_Grid[1][0]")
        self.assertEqual(self.AdventOfCodeDay06Inst.Light_Grid[1][1], True, "Light_Grid[1][1]")
        self.assertEqual(self.AdventOfCodeDay06Inst.Light_Grid[2][0], False, "Light_Grid[2][0]")
        self.assertEqual(self.AdventOfCodeDay06Inst.Light_Grid[2][1], True, "Light_Grid[2][1]")

    def __assert_lights_values(self, source, dest, expected_value):
        for i in range(source[0], dest[0] + 1):
            for j in range(source[1], dest[1] + 1):
                self.assertEqual(self.AdventOfCodeDay06Inst.Light_Grid[i][j], expected_value, "Light_Grid[{0}][{1}]".format(i, j))


class LightGridCommand(Enum):
    TurnOn = 0
    TurnOff = 1
    Toggle = 2


class AdventOfCodeDay06Base(object):
    def process_command(self, command_text):
        command_info = self.__get_command_info(command_text)
        if command_info['command'] == LightGridCommand.TurnOn:
            self.turn_on(command_info['source'], command_info['dest'])
        elif command_info['command'] == LightGridCommand.TurnOff:
            self.turn_off(command_info['source'], command_info['dest'])
        elif command_info['command'] == LightGridCommand.Toggle:
            self.toggle(command_info['source'], command_info['dest'])

    def toggle(self, source, dest):
        pass

    def turn_on(self, source, dest):
        pass

    def turn_off(self, source, dest):
        pass

    def __get_command_info(self, command_text):
        grid_command = self.__get_grid_command(command_text)
        command_text_segments = command_text.split(' ')
        point_indices = self.__get_point_segment_indices(grid_command)
        source_point = self.__get_point(command_text_segments[point_indices[0]])
        dest_point = self.__get_point(command_text_segments[point_indices[1]])
        return { 'command' : grid_command, 'source' : source_point, 'dest' : dest_point }

    def __get_point_segment_indices(self, grid_command):
        if grid_command == LightGridCommand.Toggle:
            return (1, 3)
        else:
            return (2, 4)

    def __get_grid_command(self, command_text):
        if command_text.startswith("turn on"):
            return LightGridCommand.TurnOn
        elif command_text.startswith("turn off"):
            return LightGridCommand.TurnOff
        elif command_text.startswith("toggle"):
            return LightGridCommand.Toggle

    def __get_point(self, point_text):
        point_segments = point_text.split(',')
        return (int(point_segments[0]), int(point_segments[1]))


class AdventOfCodeDay06OnOff(AdventOfCodeDay06Base):
    def __init__(self):
        self.Light_Grid = [[False for i in range(1000)] for j in range(1000)]

    def turn_on(self, source, dest):
        self.__set_lights(source, dest, True)

    def turn_off(self, source, dest):
        self.__set_lights(source, dest, False)

    def toggle(self, source, dest):
        for i in range(source[0], dest[0] + 1):
            for j in range(source[1], dest[1] + 1):
                self.Light_Grid[i][j] = not self.Light_Grid[i][j]

    def __set_lights(self, source, dest, value):
        for i in range(source[0], dest[0] + 1):
            for j in range(source[1], dest[1] + 1):
                self.Light_Grid[i][j] = value


class AdventOfCodeDay06Brightnes(AdventOfCodeDay06Base):
    def __init__(self):
        self.Light_Grid = [[0 for i in range(1000)] for j in range(1000)]

    def turn_on(self, source, dest):
        self.__set_lights(source, dest, 1)

    def turn_off(self, source, dest):
        self.__set_lights(source, dest, -1)

    def toggle(self, source, dest):
        self.__set_lights(source, dest, 2)

    def __set_lights(self, source, dest, value):
        for i in range(source[0], dest[0] + 1):
            for j in range(source[1], dest[1] + 1):
                self.Light_Grid[i][j] = max(self.Light_Grid[i][j] + value, 0)


def main():
    advent_day_06_on_off = AdventOfCodeDay06OnOff()
    advent_day_06_brightness = AdventOfCodeDay06Brightnes()
    with open("input/day_06.txt", "r") as inputFile:
        for command_text in inputFile:
            advent_day_06_on_off.process_command(command_text)
            advent_day_06_brightness.process_command(command_text)
    light_on_count = 0
    brightness = 0
    for i in range(len(advent_day_06_on_off.Light_Grid)):
        for j in range(len(advent_day_06_on_off.Light_Grid[0])):
            if advent_day_06_on_off.Light_Grid[i][j]:
                light_on_count += 1
            brightness += advent_day_06_brightness.Light_Grid[i][j]
    print("lights on: ", light_on_count)
    print("brightness: ", brightness)


if __name__ == "__main__":
    main()