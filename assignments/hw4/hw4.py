"""
Name: <Lindsay Spratt>
<hw4>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating graphics for fun, or mathematical use and further approximating pi and finding the accuracy of both methods.
Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    win.setBackground("white")

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(100, 100), Point(150, 150))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to create squares
    for i in range(num_clicks):
        click = win.getMouse()
        p_value_x = click.getX()
        p_value_x2 = click.getX()
        p_value_y = click.getY()
        p_value_y2 = click.getY()
        shape = Rectangle(Point(p_value_x + 50, p_value_y), (Point(p_value_x2, p_value_y2 + 50)))
        shape.move(-25, -25)
        shape.setFill("red")
        shape.draw(win)
    end_click = 1
    inst_pt2 = Point(width / 2, height - 30)
    instructions2 = Text(inst_pt2, "Click again to close")
    instructions2.draw(win)
    win.getMouse()
    win.close()

def rectangle():
    # create window
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    win.setCoords(0.0, 0.0, 20, 20)
    message = Text(Point(10, 0.5), "Click on two opposite points to create a rectangle")
    message.draw(win)
    # store clicks
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    # modify visuals
    rectangle_draw = Rectangle(p1, p2)
    rectangle_draw.setFill("green")
    rectangle_draw.setOutline("black")
    rectangle_draw.draw(win)
    # perimeter & area formulas
    length = abs(p2.getX() - abs(p1.getX()))
    width = abs(p2.getY() - abs(p1.getY()))
    perimeter = (length * 2) + (width * 2)
    area = (length) * (width)
    per_display = Text(Point(10, 15), "Perimeter:" + str(perimeter))
    per_display.draw(win)
    area_message = Text(Point(10, 16), "Area:" + str(area))
    area_message.draw(win)
    close_message = Text(Point(10, 14), "Click again to close")
    close_message.draw(win)
    win.getMouse()
    win.close()
def circle():
    # creating window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
    win.setBackground("white")
    # instructions for clicking and storing clicks
    inst = Text(Point(200, 200), "Click anywhere to choose the center of the circle")
    inst.draw(win)
    p1 = win.getMouse()
    inst_2 = Text(Point(200, 210), "Click again to create the circle")
    inst_2.draw(win)
    p2 = win.getMouse()
    # storing x,y of clicks
    p1x_value = p1.getX()
    p1y_value = p1.getY()
    p2x_value = p2.getX()
    p2y_value = p2.getY()
    # Euclidean formula & display circle
    radius1 = ((p2x_value - p1x_value)**2) + ((p2y_value-p1y_value)**2)
    radius2 = math.sqrt(radius1)
    circle_create = Circle(Point(p1x_value, p1y_value), radius2)
    circle_create.draw(win)
    circle_create.setFill("green")
    # radius message
    rad_display = Text(Point(200, 380), "Radius: " + str(radius2))
    rad_display.draw(win)
    # click to exit
    click_exit = Text(Point(200, 240), "Click to close")
    click_exit.draw(win)
    win.getMouse()
    win.close()

def pi2():
    total = 0
    num = eval(input("Please enter the number of terms you would like to sum: "))
    for i in range(0, num, 2):
        total += ((1.0 / (i + i + 1)) - 1.0 / (i + i + 3))
    total = 4 * total
    print("pi approximation: ", total)
    accuracy = math.pi - total
    print("accuracy: ", accuracy)
if __name__ == '__main__':
    squares()
    rectangle()
    circle()
    pi2()