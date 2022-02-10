"""
Name: <Lindsay Spratt>
<lab4>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Valentine's day card for fun!
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from graphics import *

def greeting_card():
    # window creation
    width = 500
    height = 500
    win = GraphWin("Happy Valentines Day", width, height)
    win.setCoords(0, 0, 20, 20)
    win.setBackground("black")

    # heart image display
    heart_image = Image(Point(10, 10), "heart.gif")
    heart_image.draw(win)

    # text 1 display
    heart_pt = Point(10, 12)
    heart_message = Text(heart_pt, "Happy Valentine's Day!")
    heart_message.setTextColor("black")
    heart_message.setFace("arial")
    heart_message.setStyle("bold italic")
    heart_message.setSize(20)
    heart_message.draw(win)

    # arrow creation
    arrow = Image(Point(0, 10), "white arrow.gif")
    arrow.draw(win)
    for i in range(1000):
        arrow.move(.1, .0001)

    # close message
    close_message = Text(Point(10, 2), "Click anywhere to close")
    close_message.setTextColor("pink")
    close_message.setFace("arial")
    close_message.setStyle("bold")
    close_message.setSize(15)
    close_message.draw(win)

    # wait for mouse
    win.getMouse()
    win.close()

greeting_card()
