"""
Name: <Lindsay Spratt>
<hw8>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using for loops, while loops, and if statements to run math equations and graphics.
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import math
from graphics import *


def add_ten(nums):
    nums[:] = [i + 10 for i in nums]


def square_each(nums):
    nums[:] = [nums[i] ** 2 for i in nums]
    return nums


def sum_list(nums):
    acc = 0
    for i in range(nums):
        acc += nums[i]
    return nums


def to_numbers(nums):
    for i in nums:
        int(i)


def sum_of_square(nums):
    for i in nums:
        int(i)
    nums[:] = [nums[i] ** 2 for i in nums]
    acc = 1
    for i in range(nums):
        acc += nums[i] ** 2
    return nums


def starter(weight, wins):
    if (150 <= weight < 160 and wins >= 5) or (weight > 199) or (wins > 20):
        return True
    else:
        return False


def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0):
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    # creating circle one
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    # creating circle two
    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)
    if did_overlap(circle_one,circle_two):
        print("The circles overlap")
    else:
        print("The circles do not overlap")
    while not win.checkMouse():
        print("Click to close")
    else:
        win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    circle_overlap()
    radius = circle_one.getRadius
    radius2 = circle_two.getRadius
    rad_sum = radius + radius2
    center = circle_one.getCenter()
    center2 = circle_two.getCenter()
    distance_part1 = (center2.getX() - center.getX() ** 2) + (center2.getY() - center.getY() ** 2)
    distance_final = math.sqrt(distance_part1)
    if distance_final <= rad_sum:
        return True
    else:
        return False


if __name__ == '__main__':
    pass
