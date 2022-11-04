from unittest import TestCase, mock, main
from api.smoothies import SmoothieManager


class TestRecipes(TestCase):

    # def test_get_recipe_data_for_ingredient(self):
    #     test_ingredient = 'mushrooms'
    #     recipe_data = Recipes.get_recipe_data_for_ingredient(test_ingredient)
    #     # Assert that there is at least one recipe
    #     self.assertGreater(len(recipe_data), 0)
    #     # Assert that at least one recipe contains the test ingredient in its title
    #     try:
    #         next(filter(lambda recipe: test_ingredient in recipe['recipe']['label'], recipe_data))
    #     except StopIteration:
    #         self.fail('Test ingredient not in any of the recipe titles')

    def test_smoothie_search_good(self):
        with mock.patch("builtins.input", side_effect=["banana"]):
            with self.assertEqual(items['banana']):
                smoothie_search()

if __name__ == '__main__':
    unittest.main()