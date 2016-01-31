import unittest
import IsOdd

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd.isOdd(1), "IsOdd(1)")

    def testTwo(self):
        self.assertFalse(IsOdd.isOdd(2), "IsOdd(2)")

def main():
    unittest.main()

if __name__ == '__main__':
    main()