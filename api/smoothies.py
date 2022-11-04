import requests
import config


class SmoothieManager:
    """manages calls to edamam API"""
    edamam_app_id = config.app_id
    edamam_app_key = config.app_key

    def get_smoothie_data(self, ingredient):
        """
        gets all data from the API endpoint
        """
        try:
            api_response = requests.get(
                    f'https://api.edamam.com/api/recipes/v2?type=public'
                    f'&q={ingredient}'
                    f'&app_id={self.edamam_app_id}'
                    f'&app_key={self.edamam_app_key}'
                    f'&diet=low-fat'
                    f'&tag=smoothie')
            return api_response.json()['hits']
        except (requests.exceptions.RequestException, KeyError):
            return []

    def smoothie_search(self, ingredient):
        """This takes an ingredient as user input and searches the API
            then it will return results"""
        smoothie_data = self.get_smoothie_data(ingredient)
        return [{
            'name': item['recipe']['label'],
            'url': item['recipe']['url'],
            'source': item['recipe']['source'],
            'diet_labels': ', '.join(item['recipe']['dietLabels'])
        } for item in smoothie_data]
