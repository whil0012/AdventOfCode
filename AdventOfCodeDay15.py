import unittest
import NamedPropertyItem


class TestAdventOfCodeDay15(unittest.TestCase):
    def get_butterscotch_named_property_item(self):
        return NamedPropertyItem.named_property_item(name="Butterscotch", capacity=-1, durability=-2, flavor=6, texture=3, calories=8)

    def get_cinnamon_named_property_item(self):
        return NamedPropertyItem.named_property_item(name="Cinnamon", capacity=2, durability=3, flavor=-2, texture=-1, calories=3)

    def test_get_all_combinations_for_100_WhenInvoked_ReturnsOnlyCombinationsThatSumTo100(self):
        actual = get_all_combinations_for_100()
        for combination in actual:
            combination_sum = sum(combination)
            self.assertEqual(combination_sum , 100, combination)

    def test_get_all_combinatins_for_100_WhenInvoked_ReturnsOnlyNumbersBetween1and97(self):
        # 97 is the maximum number that can be in a combination with 3 other numbers greater than 0, i.e. [1, 1, 1, 97]
        actual = get_all_combinations_for_100()
        for combination in actual:
            for number in combination:
                self.assertTrue(number >= 1, "number: " + str(number) + "; combination: " + str(combination))
                self.assertTrue(number <= 97, "number: " + str(number) + "; combination: " + str(combination))

    def test_get_score_WhenButterscotchAndCinnamon_ReturnsCorrectScore(self):
        butterscotch = self.get_butterscotch_named_property_item()
        cinnamon = self.get_cinnamon_named_property_item()
        recipe = [(butterscotch, 44), (cinnamon, 56)]
        actual = get_recipe_score(recipe)
        self.assertEqual(actual, 62842880)



def get_all_combinations_for_100():
    for first_number in range(1, 98):
        for second_number in range(1, 99 - first_number):
            for third_number in range(1, 100 - (first_number + second_number)):
                yield [first_number, second_number, third_number, 100 - (first_number + second_number + third_number)]


def get_capacity(recipe_item):
    return recipe_item[0].capacity * recipe_item[1]


def get_durability(recipe_item):
    return recipe_item[0].durability * recipe_item[1]


def get_flavor(recipe_item):
    return recipe_item[0].flavor * recipe_item[1]


def get_texture(recipe_item):
    return recipe_item[0].texture * recipe_item[1]


def get_calories(recipe_item):
    return recipe_item[0].calories * recipe_item[1]


def get_recipe_score(recipe):
    scores = [0, 0, 0, 0]
    calories = 0
    for recipe_item in recipe:
        scores[0] += get_capacity(recipe_item)
        scores[1] += get_durability(recipe_item)
        scores[2] += get_flavor(recipe_item)
        scores[3] += get_texture(recipe_item)
        calories += get_calories(recipe_item)
    if any(score <= 0 for score in scores):
        total_score = 0
    else:
        total_score = scores[0] * scores[1] * scores[2] * scores[3]
    return NamedPropertyItem.named_property_item(score = total_score, calories=calories)


sprinkles = NamedPropertyItem.named_property_item(name="Sprinkles", capacity=5, durability=-1, flavor=0, texture=0, calories=5)
peanut_butter = NamedPropertyItem.named_property_item(name="PeanutButter", capacity=-1, durability=3, flavor=0, texture=0, calories=1)
frosting = NamedPropertyItem.named_property_item(name="Frosting", capacity=0, durability=-1, flavor=4, texture=0, calories=6)
sugar = NamedPropertyItem.named_property_item(name="Sugar", capacity=-1, durability=0, flavor=0, texture=2, calories=8)


def main():
    four_ingredient_amount_combinations = get_all_combinations_for_100()
    max_score = 0
    max_score_at_500_calories = 0
    for combination in four_ingredient_amount_combinations:
        recipe = [(sprinkles, combination[0]), (peanut_butter, combination[1]), (frosting, combination[2]), (sugar, combination[3])]
        score = get_recipe_score(recipe)
        if score.score > max_score:
            max_score = score.score
        if score.calories == 500:
            if score.score > max_score_at_500_calories:
                max_score_at_500_calories = score.score
    print("max score: ", max_score)
    print("max score at 500 calories: ", max_score_at_500_calories)


if __name__ == "__main__":
    main()
