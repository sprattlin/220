"""
Name: <Lindsay Spratt>
<hw10>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using while loops and if statements for math equations, and creating classes for
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from face import Face
from sphere import Sphere
import math


def fibonacci(n):
    while n < 1:
        return None
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def double_investment(principle, rate):     # int object is not callable
    n = 0
    a = principle(n + (rate/100))
    while a < (2 * a):
        n += 1
        return n


def syracuse(n):
    syracuse_list = []
    while n != 1:
        if n % 2 == 0:
            syracuse_list.append(n / 2)
        else:
            syracuse_list.append((3 * n) + 1)
    return syracuse_list


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