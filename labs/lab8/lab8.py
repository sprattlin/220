"""
Name: <Lindsay Spratt>
<lab8>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using graphics, if statements and while loops to create a fun simulation (:
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import*
import math

def get_random(move_amount):
    random = randint(-move_amount, +move_amount)
    return random


def did_collide(circle_ball, circle_ball2):
    # circle 1 point one
    circ_1_point = circle_ball.getCenter()
    circ_1_x = circ_1_point.getX()
    circ_1_y = circ_1_point.getY()
    # circle 2 point 1
    circ_2_point = circle_ball2.getCenter()
    circ_2_x = circ_2_point.getX()
    circ_2_y = circ_2_point.getY()
    # math distance formulas
    dist_circle = (circ_2_x - circ_1_x)**2 + (circ_2_y - circ_1_y)**2
    distance_circ_square = math.sqrt(dist_circle)
    # radius of circles
    rad_1 = circle_ball.getRadius()
    rad_2 = circle_ball2.getRadius()
    rad_sum = rad_2 + rad_1    # int object not iterable
    if distance_circ_square <= rad_sum:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    center = circle_ball.getCenter()
    y_int = center.getY()
    rad = circle_ball.getRadius()
    bottom = y_int + rad
    top = y_int - rad
    y_int_win = win.getHeight()
    if top <= 0 or bottom >= y_int_win:
        return True
    else:
        return False

def hit_horizontal(circle_ball, win):
    center = circle_ball.getCenter()
    x_int = center.getX()
    rad = circle_ball.getRadius()
    side_left = x_int - rad
    side_right = x_int + rad
    x_int_win = win.getWidth()
    if side_right >= x_int_win or side_left <= 0:
        return True
    else:
        return False


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = color_rgb(r, g, b)
    return color


def bumper():
    # create window
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    # create random points for circle
    rand_point_1 = randint(0, 700)
    rand_point_2 = randint(0, 700)
    rand_center = randint(10, 50)
    # create circle
    circle_ball = Circle(Point(rand_point_1, rand_point_2), rand_center)
    circle_ball.setFill(get_random_color())
    circle_ball.draw(win)
    # create random points for circle 2
    circ_rand_3 = randint(0, 700)
    circ_rand_4 = randint(0, 700)
    circ_2_center = randint(10, 50)
    # create circle 2
    circle_ball2 = Circle(Point(circ_rand_3, circ_rand_4), circ_2_center)
    circle_ball2.setFill(get_random_color())
    circle_ball2.draw(win)
    # move circles randomly
    dy = get_random(50)
    dx = get_random(50)
    dy_2 = get_random(50)
    dx_2 = get_random(50)
    # to make sure user has not clicked
    while not win.checkMouse():
        time.sleep(0.1)
        circle_ball.move(dx, dy)
        circle_ball2.move(dx_2, dy_2)
    # making circles bounce away if they hit a wall or each other
        if hit_horizontal(circle_ball, win):
            dx = -dx

        if hit_horizontal(circle_ball2, win):
            dx_2 = -dx_2

        if hit_vertical(circle_ball, win):
            dy = -dy
        if hit_vertical(circle_ball2, win):
            dy_2 = -dy_2
        if did_collide(circle_ball, circle_ball2):
            dx = -dx
            dy = -dy
            dx_2 = -dx_2
            dy_2 = -dy_2

    else:
        win.close()


bumper()


