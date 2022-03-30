"""
Name: <Lindsay Spratt>
<door>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
making door class
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from graphics import *

class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)
        self.secret = False
    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.draw.undraw()
        self.text.draw.undraw()

    def is_clicked(self, point):
        point_1 = self.shape.getP1()
        point_2 = self.shape.getP2()
        point_1_x = point_1.getX()
        point_2_x = point_2.getX()
        point_1_y = point_1.getY()
        point_2_y = point_2.getY()
        if point_1_x <= point.getX() <= point_2_x and point_1_y <= point.getY() <= point_2_y:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret


