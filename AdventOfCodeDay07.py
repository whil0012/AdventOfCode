import unittest

from setuptools.compat import basestring

from numbers import Number


class TestAdventOfCodeDay07(unittest.TestCase):
    def setUp(self):
        self.AdventOfCodeDay07Inst = AdventOfCodeDay07()

    def testNot16Bit_WhenInvoked_ReturnsBitwiseNot(self):
        actual = AdventOfCodeDay07.not_16_bit(123)
        self.assertEqual(actual, 65412)

    def testProcessCommand_Assign_SetsValue(self):
        self.AdventOfCodeDay07Inst.process_command("123 -> x")
        actual = self.AdventOfCodeDay07Inst.get_value("x")
        self.assertEqual(actual, 123)

    def testProcessCommand_AssignWireValue_SetsValue(self):
        self.AdventOfCodeDay07Inst.process_command("123 -> x")
        self.AdventOfCodeDay07Inst.process_command("x -> y")
        actual = self.AdventOfCodeDay07Inst.get_value("y")
        self.assertEqual(actual, 123)

    def testProcessCommand_Not_AssignsNotVale(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.process_command("NOT x -> h")
        actual = self.AdventOfCodeDay07Inst.get_value("h")
        self.assertEqual(actual, 65412)

    def testProcessCommand_And_AssignsAndValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.process_command("x AND y -> d")
        actual = self.AdventOfCodeDay07Inst.get_value("d")
        self.assertEqual(actual, 72)

    def testProcessCommand_Or_AssignsOrValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.process_command("x OR y -> e")
        actual = self.AdventOfCodeDay07Inst.get_value("e")
        self.assertEqual(actual, 507)

    def testProcessCommand_LeftShift_AssignsLeftShiftValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.process_command("x LSHIFT 2 -> f")
        actual = self.AdventOfCodeDay07Inst.get_value("f")
        self.assertEqual(actual, 492)

    def testProcessCommand_RightShift_AssignsRightShiftValue(self):
        self.AdventOfCodeDay07Inst.set_value("x", 123)
        self.AdventOfCodeDay07Inst.set_value("y", 456)
        self.AdventOfCodeDay07Inst.process_command("y RSHIFT 2 -> g")
        actual = self.AdventOfCodeDay07Inst.get_value("g")
        self.assertEqual(actual, 114)


class AdventOfCodeDay07(object):
    not_16_bit_mask = 0xFFFF

    def __init__(self):
        self.__Wire_Values = {}

    @staticmethod
    def not_16_bit(value):
        return value ^ AdventOfCodeDay07.not_16_bit_mask

    def process_command(self, command_text):
        command_segments = command_text.split()
        if self.__is_assign_command(command_segments):
            self.__process_assign_command(command_segments)
        elif self.__is_not_command(command_segments):
            self.__process_not_command(command_segments)
        elif self.__is_and_command(command_segments):
            self.__process_and_command(command_segments)
        elif self.__is_or_command(command_segments):
            self.__process_or_command(command_segments)
        elif self.__is_left_shift_command(command_segments):
            self.__process_left_shift_command(command_segments)
        elif self.__is_right_shift_command(command_segments):
            self.__process_right_shift_command(command_segments)

    def __process_and_command(self, command_segments):
        self.__process_binary_command(command_segments, lambda x: self.get_value(x), lambda x, y: x & y)

    def __process_or_command(self, command_segments):
        self.__process_binary_command(command_segments, lambda x: self.get_value(x), lambda x, y: x | y)

    def __process_left_shift_command(self, command_segments):
        self.__process_binary_command(command_segments, lambda x: int(x), lambda x, y: x << y)

    def __process_right_shift_command(self, command_segments):
        self.__process_binary_command(command_segments, lambda x: int(x), lambda x, y: x >> y)

    def __process_binary_command(self, command_segments, interpret_second_argument_function, binary_function):
        input_wire_1 = command_segments[0]
        input_wire_2 = command_segments[2]
        output_wire = command_segments[4]
        input_value_1 = self.get_value(input_wire_1)
        input_value_2 = interpret_second_argument_function(input_wire_2)
        output_value = binary_function(input_value_1, input_value_2)
        self.set_value(output_wire, output_value)

    def __process_assign_command(self, command_segments):
        value = command_segments[0]
        if value.isdigit():
            wire_value = int(value)
        else:
            wire_value = self.get_value(value)
        wire_name = command_segments[2]
        self.set_value(wire_name, wire_value)

    def __process_not_command(self, command_segments):
        input_wire_name = command_segments[1]
        output_wire_name = command_segments[3]
        input_value = self.get_value(input_wire_name)
        not_value = AdventOfCodeDay07.not_16_bit(input_value)
        self.set_value(output_wire_name, not_value)

    def __is_command_text(self, command, command_text_to_compare):
        return isinstance(command, basestring) and (command.casefold() == command_text_to_compare.casefold())

    def __is_assign_command(self, command_segments):
        return command_segments[1] == "->"

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

    def get_value(self, wire_name):
        return self.__Wire_Values[wire_name]

    def set_value(self, wire_name, value):
        self.__Wire_Values[wire_name] = value


def main():
    # This isn't working. The specifications are not
    # guaranteed to be in any specific order.
    # TODO: Update unit tests to have a test "out of order"
    # TODO: Update implementation to store references
    #       instead of actual values, and evaluate the
    #       reference when needed.
    #       Optional: Store evaluated reference to avoid
    #       evaluating a second time for the same circuits
    #       sections.
    advent_day_07_inst = AdventOfCodeDay07()
    with open("input/day_07.txt", "r") as inputFile:
        for command_text in inputFile:
            advent_day_07_inst.process_command(command_text)
    print("signal wire a: ", advent_day_07_inst.Wire_Values["a"])


if __name__ == "__main__":
    main()