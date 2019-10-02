""""
Program: inner_functions_assignment
Author: Kelly Smith
Last date updated: 10/01/19

Program to output the area and perimeter of a rectangle or square
"""


def measurements():
    a_list = [3.5]

    def area():
        a_list
        if len(a_list) == 2:
            print('Area = ', a_list[0] * a_list[1])
        else:
            print('Area = ', a_list[0] * a_list[0])

    def perimeter():
        a_list
        if len(a_list) == 2:
            print('Perimeter = ', (a_list[0] * 2) + (a_list[1] * 2))
        else:
            print('Perimeter = ', a_list[0] * 4)

    area()
    perimeter()


if __name__ == '__main__':
    print(measurements())
