import unittest

from setuptools.compat import basestring

from numbers import Number


class TestAdventOfCodeDay07(unittest.TestCase):
    def setUp(self):
        self.AdventOfCodeDay07Inst = AdventOfCodeDay07()

    def testNot16Bit_WhenInvoked_ReturnsBitwiseNot(self):
        actual = AdventOfCodeDay07.not_16_bit(123)
        self.assertEqual(actual, 65412)

    def testAddCommand_Assign_SetsValue(self):
        self.AdventOfCodeDay07Inst.add_command("123 -> x")
        actual = self.AdventOfCodeDay07Inst.get_value("x")
        self.assertEqual(actual, 123)

    def testAddCommand_AssignWireValue_SetsValue(self):
        self.AdventOfCodeDay07Inst.add_command("x -> y")
        self.AdventOfCodeDay07Inst.add_command("123 -> x")
        actual = self.AdventOfCodeDay07Inst.get_value("y")
        self.assertEqual(actual, 123)

    def testAddCommand_Not_AssignsNotVale(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.add_command("NOT x -> h")
        actual = self.AdventOfCodeDay07Inst.get_value("h")
        self.assertEqual(actual, 65412)

    def testAddCommand_And_AssignsAndValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.add_command("x AND y -> d")
        actual = self.AdventOfCodeDay07Inst.get_value("d")
        self.assertEqual(actual, 72)

    def testAddCommand_Or_AssignsOrValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.add_command("x OR y -> e")
        actual = self.AdventOfCodeDay07Inst.get_value("e")
        self.assertEqual(actual, 507)

    def testAddCommand_LeftShift_AssignsLeftShiftValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.add_command("x LSHIFT 2 -> f")
        actual = self.AdventOfCodeDay07Inst.get_value("f")
        self.assertEqual(actual, 492)

    def testAddCommand_RightShift_AssignsRightShiftValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.add_command("y RSHIFT 2 -> g")
        actual = self.AdventOfCodeDay07Inst.get_value("g")
        self.assertEqual(actual, 114)

    def testAddCommand_WhenOutOfOrders_SetsCorrectValue(self):
        self.AdventOfCodeDay07Inst.add_command("y RSHIFT 2 -> g")
        self.AdventOfCodeDay07Inst.add_command("456 -> y")
        self.AdventOfCodeDay07Inst.add_command("123 -> x")
        actual = self.AdventOfCodeDay07Inst.get_value("g")
        self.assertEqual(actual, 114)

    def testAndCommand_WhenLeftOpIsDigit_SetsCorrectValue(self):
        self.AdventOfCodeDay07Inst.add_command("7 and x -> a")
        self.AdventOfCodeDay07Inst.add_command("123 -> x")
        actual = self.AdventOfCodeDay07Inst.get_value("a")
        self.assertEqual(actual, 3)


class AdventOfCodeDay07(object):
    not_16_bit_mask = 0xFFFF

    def __init__(self):
        self.__Wire_Values = {}
        self.__Wire_Command_Texts = {}

    @staticmethod
    def not_16_bit(value):
        return value ^ AdventOfCodeDay07.not_16_bit_mask

    def add_command(self, command_text):
        command_segments = [x.strip() for x in command_text.split("->")]
        command_text = command_segments[0]
        wire_name = command_segments[1]
        self.__set_command_text(wire_name, command_text)

    def __process_command(self, command_text):
        command_segments = command_text.split()
        if self.__is_assign_command(command_segments):
            return self.__process_assign_command(command_segments)
        elif self.__is_not_command(command_segments):
            return self.__process_not_command(command_segments)
        elif self.__is_and_command(command_segments):
            return self.__process_and_command(command_segments)
        elif self.__is_or_command(command_segments):
            return self.__process_or_command(command_segments)
        elif self.__is_left_shift_command(command_segments):
            return self.__process_left_shift_command(command_segments)
        elif self.__is_right_shift_command(command_segments):
            return self.__process_right_shift_command(command_segments)

    def __process_and_command(self, command_segments):
        return self.__process_binary_command(command_segments, lambda x: self.get_value(x), lambda x, y: x & y)

    def __process_or_command(self, command_segments):
        return self.__process_binary_command(command_segments, lambda x: self.get_value(x), lambda x, y: x | y)

    def __process_left_shift_command(self, command_segments):
        return self.__process_binary_command(command_segments, lambda x: int(x), lambda x, y: x << y)

    def __process_right_shift_command(self, command_segments):
        return self.__process_binary_command(command_segments, lambda x: int(x), lambda x, y: x >> y)

    def __process_binary_command(self, command_segments, interpret_second_argument_function, binary_function):
        input_wire_1 = command_segments[0]
        input_wire_2 = command_segments[2]
        input_value_1 = self.get_value(input_wire_1)
        input_value_2 = interpret_second_argument_function(input_wire_2)
        output_value = binary_function(input_value_1, input_value_2)
        return output_value

    def __process_assign_command(self, command_segments):
        value = command_segments[0]
        if value.isdigit():
            wire_value = int(value)
        else:
            wire_value = self.get_value(value)
        return wire_value

    def __process_not_command(self, command_segments):
        input_wire_name = command_segments[1]
        input_value = self.get_value(input_wire_name)
        not_value = AdventOfCodeDay07.not_16_bit(input_value)
        return not_value

    def __is_command_text(self, command, command_text_to_compare):
        return isinstance(command, basestring) and (command.casefold() == command_text_to_compare.casefold())

    def __is_assign_command(self, command_segments):
        return len(command_segments) == 1

    def __is_not_command(self, command_segments):
        return self.__is_command_text(command_segments[0], "not")

    def __is_and_command(self, command_segments):
        return self.__is_command_text(command_segments[1], "and")

    def __is_or_command(self, command_segments):
        return self.__is_command_text(command_segments[1], "or")

    def __is_left_shift_command(self, command_segments):
        return self.__is_command_text(command_segments[1], "lshift")

    def __is_right_shift_command(self, command_segments):
        return self.__is_command_text(command_segments[1], "rshift")

    def get_value(self, wire_name_or_value):
        if wire_name_or_value.isdigit():
            return int(wire_name_or_value)
        if not self.__wire_value_set(wire_name_or_value):
            self.__process_and_set_wire_value(wire_name_or_value)
        return self.__get_wire_value(wire_name_or_value)

    def __wire_value_set(self, wire_name):
        return wire_name in self.__Wire_Values

    def __get_wire_value(self, wire_name):
        return self.__Wire_Values[wire_name]

    def __process_and_set_wire_value(self, wire_name):
        command_text = self.__get_command_text(wire_name)
        value = self.__process_command(command_text)
        self.set_value(wire_name, value)

    def set_value(self, wire_name, value):
        self.__Wire_Values[wire_name] = value

    def __set_command_text(self, wire_name, command_text):
        self.__Wire_Command_Texts[wire_name] = command_text

    def __get_command_text(self, wire_name):
        return self.__Wire_Command_Texts[wire_name]

    def clear_values(self):
        self.__Wire_Values = {}


def main():
    advent_day_07_inst = AdventOfCodeDay07()
    with open("input/day_07.txt", "r") as inputFile:
        for command_text in inputFile:
            advent_day_07_inst.add_command(command_text)
    wire_a_value = advent_day_07_inst.get_value("a")
    print("signal wire a: ", wire_a_value)
    advent_day_07_inst.clear_values()
    advent_day_07_inst.set_value("b", wire_a_value)
    wire_a_value = advent_day_07_inst.get_value("a")
    print("new signal wire a: ", wire_a_value)


if __name__ == "__main__":
    main()