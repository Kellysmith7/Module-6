"""
Program: validate_input_in_functions.py
Author: Kelly Smith
Last date updated: 10/01/19


Program to output a test name and score
:param test_name: this is the test name this is mandatory
:param score: this is the test score must be between 0 and 100
:param invaild_message: this gives a messasge if a score is not vaild
:returns: Test name and test score
"""


def score_input(prompt, test_score=0, invalid_message='Invalid test score, try again!'):
    test_name = input(prompt)
    if 0 <= test_score <= 100:
        print(test_name, test_score)
    else:
        print(invalid_message)
    #return {test_name: test_score}
    #return pass


if __name__ == '__main__':
    score_input('Math', 20)
