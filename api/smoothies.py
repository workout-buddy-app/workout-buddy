import json
import requests
import functools


class SmoothieManager:
    """
    manages the call to the API
    """
    app_id = 'ea19623b'
    app_key = '77db48d61cf003a1d873a3609ce6e79d'
    smoothie_endpoint = f'https://api.edamam.com/api/recipes/v2?type=public&q=smoothie&app_id={app_id}&app_key={app_key}'


    def __init__(self):
        self.smoothie_data = self.get_smoothie_data()

    def get_smoothie_data(self):
        """
        gets all data from the API endpoint
        """
        smoothie_results = requests.get(url=self.smoothie_endpoint)
        smoothie_data = smoothie_results.json()
        return smoothie_data['hits']

    def smoothie_search(self, ingredient):
        """This takes an ingredient as user input and searches the API
            then it will return results"""
        ingredient = input('Enter an ingredient to search ')
        search_results = self.smoothie_data
        for item in search_results:
            items = item['recipe']
            result_values = items['label'], items['uri'], 'CAUTIONS: ', items['cautions'], 'DIETARY LABELS: ', items[
                'dietLabels']
            print(*result_values, sep='\n')

    @functools.cache
    def get_smoothie_search_data(self, ingredient):
        """gets category data and checks if its seen it before
         if not then will talk to api"""
        smoothie_ingredient_response = self.smoothie_data
        smoothie_search_data = smoothie_ingredient_response.json()
        return smoothie_search_data

