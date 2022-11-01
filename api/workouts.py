import requests
import random
import functools


class WorkoutManager:
    """manages calls to the workout api"""
    workout_endpoint = "https://wger.de/api/v2/exercise/"
    workout_category_endpoint = "https://wger.de/api/v2/exercisecategory/"

    # api has two languages German 1, English 2
    english_parameters = {
        "language": 2
    }

    def __init__(self):
        self.workout_data = self.get_workout_data()

    def generate_random_workouts(self):
        """gets seven random exercises from api and stores in list"""
        workout_data_random = random.sample(self.workout_data, k=7)
        workouts_to_return = []
        for workout in workout_data_random:
            workout_category_data = self.get_workout_category_data(workout['category'])
            workouts_to_return.append({'name': workout['name'], 'category': workout_category_data['name'], 'description': workout['description']})
        return workouts_to_return

    def get_workout_data(self):
        """gets exercises data from api"""
        workout_response = requests.get(url=self.workout_endpoint, params=self.english_parameters)
        workout_data = workout_response.json()
        return workout_data['results']

    @functools.cache
    def get_workout_category_data(self, category):
        """gets category data and checks if its seen it before if not then will talk to api"""
        workout_category_response = requests.get(url=self.workout_category_endpoint + str(category),
                                                 params=self.english_parameters)
        workout_category_data = workout_category_response.json()
        return workout_category_data


workout_manager = WorkoutManager()
print(workout_manager.generate_random_workouts())