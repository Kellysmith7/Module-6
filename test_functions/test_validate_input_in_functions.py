import unittest
from more_functions import validate_input_in_functions
from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input('Math'), ('Math', 0))

    def test_score_valid(self):
        self.assertEqual(score_input('Math', 20), ('Math', 20))

    def test_score_below_range(self):
        self.assertEqual(score_input('Math', -1), 'Invalid test score, try again!')

    def test_score_above_range(self):
        self.assertEqual(score_input('Math', 120), 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertEqual(score_input('Math', 'a'), 'Please enter a valid score')


if __name__ == '__main__':
    unittest.main()
