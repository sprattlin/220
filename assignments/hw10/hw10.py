"""
Name: <Lindsay Spratt>
<hw10>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using while loops and if statements for math equations, and creating classes for
Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with Ashley Woods
"""
from graphics import *
from face import Face
from sphere import Sphere
import math


def fibonacci(n):   # 1, 1, 2, 3, 5, 8
    if n < 1:
        return None
    else:
        acc = 1
        acc += acc


def double_investment(principle, rate):  # int object is not callable
    final_amount = principle
    years = 0
    while final_amount < 2 * principle:
        years = years + 1
        interest = final_amount * rate / 100.0
        final_amount += interest
        return years


def syracuse(n):
    lst = []
    while n != 1:
        lst.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    lst.append(n)
    return lst


def goldbach(n):
    if n % 2 == 0:
        return None
    else:
        half = int(math.sqrt(n))
        set_num = 2
        while set_num <= half and n % set_num != 0:
            set_num += 1


def call():
    run_sphere = Sphere(5)
    return run_sphere


def main():
    win = GraphWin('Face', 700, 700)
    center = Point(350, 350)
    size = 300
    my_face = Face(win, center, size)
    my_face.wink()
    win.getMouse()
    win.close()


if __name__ == '__main__':
    pass