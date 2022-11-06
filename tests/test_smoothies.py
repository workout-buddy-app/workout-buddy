from unittest import TestCase, main
from api.smoothies import SmoothieManager


class TestRecipes(TestCase):

    def test_smoothie_search(self):
        smoothie_manager = SmoothieManager()
        test_ingredient = 'banana'
        smoothie_data = smoothie_manager.get_smoothie_data(test_ingredient)
        # Assert that there is at least one recipe
        self.assertGreater(len(smoothie_data), 0)
        # Assert that at least one recipe contains the test ingredient in its title
        try:
            next(filter(lambda recipe: test_ingredient in smoothie_data['ingredient'] == 'Banana', smoothie_data))
        except StopIteration:
            self.fail('Test ingredient not in any of the recipe titles')


if __name__ == '__main__':
    main()
