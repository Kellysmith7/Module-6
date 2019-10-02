""""
Program: inner_functions_assignment
Author: Kelly Smith
Last date updated: 10/01/19

Program to output the area and perimeter of a rectangle
"""


def measurements():
    side_one = float(input('How long is your rectangle '))
    side_two = float(input('How tall is your rectangle '))
    a_list = [side_one, side_two]

    def area():
        a_list
        print('Area = ', side_one * side_two)

    def perimeter():
        a_list
        print('Perimeter = ', (side_one * 2) + (side_two * 2))
    area()
    perimeter()


if __name__ == '__main__':
    print(measurements())
