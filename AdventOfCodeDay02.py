import unittest


class TestAdventOfCodeDay02(unittest.TestCase):
    def testCalculateWrappingPaperFootage_2x3x4_Returns58(self):
        actual = calculate_wrapping_paper_footage([2, 3, 4])
        self.assertEqual(actual, 58)

    def testCalculateWrappingPaperFootage_1x1x10_Returns43(self):
        actual = calculate_wrapping_paper_footage([1, 1, 10])
        self.assertEqual(actual, 43)

    def testCalculateWrappingPaperFootageFromDimensions_2x3x4_Returns58(self):
        actual = calculate_wrapping_paper_footage_from_dimensions("2x3x4")
        self.assertEqual(actual, 58)

    def testCalculateRibbonFootage_2x3x4_Returns34(self):
        actual = calculate_ribbon_footage([2, 3, 4])
        self.assertEqual(actual, 34)

    def testCalculateRibbonFootage_3x2x4_Returns34(self):
        actual = calculate_ribbon_footage([3, 2, 4])
        self.assertEqual(actual, 34)

    def testCalculateRibbonFootage_1x1x10_Returns14(self):
        actual = calculate_ribbon_footage([1, 1, 10])
        self.assertEqual(actual, 14)

    def testCalculateRibbonFootageFromDimensions_2x3x4_Returns34(self):
        actual = calculate_ribbon_footage_from_dimensions("2x3x4")
        self.assertEqual(actual, 34)


def calculate_wrapping_paper_footage(sides):
    side1 = sides[0] * sides[1]
    side2 = sides[0] * sides[2]
    side3 = sides[1] * sides[2]
    smallest_side = min(side1, side2, side3)
    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    surface_area += smallest_side
    return surface_area


def calculate_ribbon_footage(sides):
    sides_copy = sides[:]
    side1 = min(sides_copy)
    sides_copy.remove(side1)
    side2 = min(sides_copy)
    footage = side1 * 2 + side2 * 2
    footage += sides[0] * sides[1] * sides[2]
    return footage


def calculate_wrapping_paper_footage_from_dimensions(dimensions):
    return calculate_wrapping_paper_footage([int(x) for x in dimensions.split('x')])


def calculate_ribbon_footage_from_dimensions(dimensions):
    return calculate_ribbon_footage([int(x) for x in dimensions.split('x')])


def main():
    total_paper_footage = 0
    total_ribbon_footage = 0
    infile = open("input\\day_02.txt", "r")
    for line in infile:
        total_paper_footage += calculate_wrapping_paper_footage_from_dimensions(line)
        total_ribbon_footage += calculate_ribbon_footage_from_dimensions(line)
    print("total square footage: ", total_paper_footage)
    print("total ribbon footage: ", total_ribbon_footage)


if __name__ == "__main__":
    main()