import json
import requests
import config


class SmoothieManager:

    def get_smoothie_data(ingredient):
        """
        gets all data from the API endpoint
        """
        api_response = requests.get(
                f'https://api.edamam.com/api/recipes/v2?type=public'
                f'&q={ingredient}'
                f'&app_id={config.app_id}'
                f'&app_key={config.app_key}'
                f'&diet=low-fat'
                f'&tag=smoothie')
        return api_response.json()['hits']


    def smoothie_search(ingredient):
        """This takes an ingredient as user input and searches the API
            then it will return results"""
        smoothie_data = SmoothieManager.get_smoothie_data(ingredient)
        if len(smoothie_data):
            for item in smoothie_data:
                items = item['recipe']
                result_values = items['label'], items['uri'], 'DIETARY LABELS: ', items[
                    'dietLabels']
                print(*result_values, sep='\n')
        else:
            print("No results found")


#SmoothieManager.smoothie_search('peach')