import unittest
from api.workouts import WorkoutManager


class TestWorkouts(unittest.TestCase):

    def test_generate_random_workouts(self):
        workout_manager = WorkoutManager()
        workout_data = workout_manager.get_workout_data()
        self.assertGreater(len(workout_data), 0)
        try:
            next(filter(lambda workout: workout['name'] == 'Axe Hold', workout_data))
        except StopIteration:
            self.fail('Axe Hold workout not available')

    def test_get_workout_category_data(self):
        workout_manager = WorkoutManager()
        workout_category_data = workout_manager.get_workout_category_data(9)
        self.assertEqual(workout_category_data['name'], 'Legs')


if __name__ == '__main__':
    unittest.main()