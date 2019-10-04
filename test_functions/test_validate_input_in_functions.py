import unittest
from more_functions import validate_input_in_functions
from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input.validate_input_in_functions)

    def test_score_valid(self):
        self.assertEqual(20, score_input.validate_input_in_functions, 20)

    def test_score_below_range(self):
        self.assertEqual(-1, score_input.validate_input_in_functions, 'Invalid test score, try again!')

    def test_score_above_range(self):
        self.assertEqual(120, score_input.validate_input_in_functions, 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertEqual(a, score_input.validate_input_in_functions, ValueError)


if __name__ == '__main__':
    unittest.main()
