"""
Name: <Lindsay Spratt>
<hw2>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    acc = 0
    y = eval(input("What is the upper bound? "))
    for i in range(0, y + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    num = 10
    for i in range (1, 11):
        print(num, 'x',)


def triangle_area():
    pass



def sum_squares():
    pass



def power():
    pass


if __name__ == '__main__':
    sum_of_threes()
    multiplication_table()


