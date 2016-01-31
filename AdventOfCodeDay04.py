import unittest
import hashlib

class TestAdventOfCodeDay04(unittest.TestCase):
    def testGetAdventCoin_abcdef_Returns609043(self):
        actual = get_advent_coin("abcdef", "00000")
        self.assertEqual(actual, 609043)

    def testGetAdventCoin_pqrstuv_Returns1048970(self):
        actual = get_advent_coin("pqrstuv", "00000")
        self.assertEqual(actual, 1048970)


def get_advent_coin(key, prefix_to_find):
    advent_coin_value = 0
    found_advent_coin = False
    prefix_length = len(prefix_to_find)
    while not found_advent_coin:
        advent_coin_value += 1
        value_to_hash = key + str(advent_coin_value)
        hash_digest = md5_hash(value_to_hash.encode('utf-8'))
        found_advent_coin = hash_digest[:prefix_length] == prefix_to_find
    return advent_coin_value


def md5_hash(value):
    md5_hasher = hashlib.md5()
    md5_hasher.update(value)
    return md5_hasher.hexdigest()


def main():
    advent_coin_value_one = get_advent_coin("iwrupvqb", "00000")
    advent_coin_value_two = get_advent_coin("iwrupvqb", "000000")
    print("advent coin one: ", advent_coin_value_one)
    print("advent coin two: ", advent_coin_value_two)


if __name__ == "__main__":
    main()