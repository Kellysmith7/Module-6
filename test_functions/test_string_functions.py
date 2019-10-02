import unittest
from topic3 import string_functions
from topic3.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_word_glue(self):
        self.assertEqual('glueglue', multiply_string.string_functions, ('glue', 2))


if __name__ == '__main__':
    unittest.main()
