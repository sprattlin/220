"""
Name: <Lindsay Spratt>
<lab5>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Graphics code and manipulating lists
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def triangle():
    width = 400
    height = 400
    win = GraphWin("Triangle", width, height)
    win.setBackground("white")

    win.setCoords(0.0, 0.0, 20, 20)
    message = Text(Point(10, 0.5), "Click three times to create a triangle")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle_create = Polygon(p1, p2, p3)
    triangle_create.draw(win)
    length_1x = abs(p2.getX()) - abs(p1.getX())
    length_1y = abs(p2.getY()) - abs(p1.getY())
    length_2x = abs(p3.getX()) - abs(p1.getX())
    length_2y = abs(p3.getY()) - abs(p1.getY())
    length_3x = abs(p3.getX()) - abs(p2.getX())
    length_3y = abs(p3.getY()) - abs(p2.getY())
    len_formula_1 = (math.sqrt((length_1x**2)) + (length_1y**2))
    len_formula_2 = (math.sqrt((length_2x**2)) + (length_2y**2))
    len_formula_3 = (math.sqrt((length_3x**2)) + (length_3y**2))
    perimeter = len_formula_1 + len_formula_2 + len_formula_3
    perimeter_message = Text(Point(10, 0.5), "Perimeter:" + str(perimeter))
    perimeter_message.draw(win)
    area_tri_1 = ((len_formula_1 + len_formula_2 + len_formula_3) / 2)
    area_tri_2 = (math.sqrt(area_tri_1 * (area_tri_1 - len_formula_1) * (area_tri_1 - len_formula_2) * (area_tri_1 - len_formula_3)))
    message.undraw()
    area_message = Text(Point(10, 1), "Area: " + str(area_tri_2))
    area_message.draw(win)
    close_message = Text(Point(10, 18), "Click to close")
    close_message.draw(win)
    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    win.getMouse()

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    color_inputs = 5
    for i in range(color_inputs):
        red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
        red_text = Text(red_text_pt, "Red: ")
        red_text.setTextColor("red")
        green_text_pt = red_text_pt.clone()
        green_text_pt.move(0, 30)
        green_text = Text(green_text_pt, "Green: ")
        green_text.setTextColor("green")
        blue_text_pt = red_text_pt.clone()
        blue_text_pt.move(0, 60)
        blue_text = Text(blue_text_pt, "Blue: ")
        blue_text.setTextColor("blue")
        red_input = Entry(Point(200, 240), 10)
        red_input.draw(win)
        green_input = Entry(Point(200, 265), 10)
        green_input.draw(win)
        blue_input = Entry(Point(200, 300), 10)
        blue_input.draw(win)
        red_text.draw(win)
        green_text.draw(win)
        blue_text.draw(win)
        win.getMouse()
        red = red_input.getText()
        green = green_input.getText()
        blue = blue_input.getText()
        converted_red = int(red)
        converted_green = int(green)
        converted_blue = int(blue)
        shape.setFill(color_rgb(converted_red, converted_green, converted_blue))

    # Wait for another click to exit
    close_message = Text(Point(200, 18), "Click to close")
    close_message.draw(win)
    win.getMouse()
    win.close()


def process_string():
    string_input = str(input("Please enter a string: "))
    char_1 = string_input[0]
    print(char_1, end=" ")
    char_last = string_input[-1]
    print(char_last, end=" ")
    char_5 = string_input[1:5]
    print(char_5, end=" ")
    concat = string_input[0] + string_input[-1]
    print(concat, end=" ")
    first_3 = string_input[0:3] * 10
    print(first_3)
    each = string_input[:]
    print(each)
    length = len(string_input)
    print(length)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = (values[1] + values[3])
    print(x)
    x = (values[0] + values[2])
    print(x)
    x = (values[1] * 5)
    print(x)
    x = [values[2], values[3], values[4]]  # error float + str
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], values[5]]  # error float and string
    print(x)
    x = values[2] + values[0] + eval(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    num_terms = eval(input("Please enter the number of terms in the series: "))
    my_list = [246]
    acc = 0
    for x in range(num_terms):
        y = 2 + (2 * (x % 3))
        print(y, end=" ")
        acc = acc + y
    print()
    print("sum: ", acc)

def target():
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Target", win_width, win_height)
    win.setBackground("white")

    y = Circle(Point(200, 200), 200)
    y.draw(win)
    y.setFill("white")
    x = Circle(Point(200, 200), 160)
    x.draw(win)
    x.setFill("black")
    z = Circle(Point(200, 200), 120)
    z.draw(win)
    z.setFill("blue")
    a = Circle(Point(200, 200), 80)
    a.draw(win)
    a.setFill("red")
    b = Circle(Point(200, 200), 40)
    b.draw(win)
    b.setFill("yellow")
    close_message = Text(Point(200, 18), "Click to close")
    close_message.draw(win)
    win.getMouse()
    win.close()
if __name__ == '__main__':
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    target()



