"""
Name: <Lindsay Spratt>
<lab10>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Calling on classes
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from graphics import *
from door import Door
from button import Button

def main():
    # create door
    win = GraphWin("Test", 1000, 1000)
    rectangle = Rectangle(Point(250, 250), Point(750, 700))
    door = Door(rectangle, "Closed")
    door.color_door('red')
    door.draw(win)
    # create button
    button_points = Rectangle(Point(250, 100), Point(750, 200))
    button_txt = Button(button_points, "Exit")
    button_txt.draw(win)

    point = win.getMouse()
    color = 'red'
    while not button_txt.is_clicked(point):
        if door.is_clicked(point):
            if color == 'white':
                door.close('red', 'Closed')
                color = 'red'
            elif color == 'red':
                door.open('white', 'Open')
                color = 'white'
        point = win.getMouse()

    win.close()

main()






