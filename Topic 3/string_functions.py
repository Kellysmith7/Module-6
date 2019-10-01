"""
Program: string_functions.py
Author: Kelly Smith
Last date updated: 9/30/19

Program to print out your favorite word your favorite number of times
:param word: this is your favorite word
:param iteration: this is your favorite number and the number of times the word will print
:returns: your favorite word is returned your favorite number of times
"""


def multiply_string():
    word = str(input("Please enter your favorite word: "))
    iteration = int(input("Please enter your favorite number: "))
    return word * iteration


if __name__ == '__main__':
    print(multiply_string())
