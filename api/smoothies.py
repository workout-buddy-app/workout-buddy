import json
import requests


def smoothie_endpoint(ingredient):
    app_id='ea19623b'
    app_key='77db48d61cf003a1d873a3609ce6e79d'
    result=requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&q=smoothie&app_id={app_id}&app_key={app_key}')
    data=result.json()
    return data['hits']


def smoothie_search():
    ingredient = input('Enter an ingredient to search ')
    search_results = smoothie_endpoint(ingredient)
    for item in search_results:
        items=item['recipe']
        result_values=items['label'], items['uri'], 'CAUTIONS: ', items['cautions'],'DIETARY LABELS: ', items['dietLabels']
        print(*result_values, sep='\n')


smoothie_search()

