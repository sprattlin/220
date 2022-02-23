"""
Name: <Lindsay Spratt>
<lab6>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating code for vigenere cipher including graphics and for loops
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from graphics import *

def vigenere():
    # creating window
    width = 400
    height = 400
    win = GraphWin("Vigenere", width, height)
    win.setBackground("white")
    # Creating entry boxes
    box_var = Entry(Point(230, 100), 20)
    code = Text(Point(100, 100), "Message to code")
    box_var.draw(win)
    code.draw(win)

    box_var_2 = Entry(Point(230, 120), 20)
    key = Text(Point(100, 120), "Enter Keyword ")
    box_var_2.draw(win)
    key.draw(win)

    # creating button
    button = Rectangle(Point(150, 200), Point(250, 250))
    button.draw(win)
    code_par = Text(Point(200, 225), "Encode")
    code_par.draw(win)
    win.getMouse()
    button.undraw()
    code_par.undraw()
    text_var_key = box_var_2.getText()  # values in box to convert
    text_var_key = text_var_key.upper()
    text_var = box_var.getText()  # values in box to convert
    text_var = text_var.upper()
    text_var = text_var.replace(" ", "")
    # looping for conversions
    empty_str = ""
    for i in range(len(text_var)):
        first_conv = ord(text_var[i]) - 65
        shift = ord(text_var_key[i % len(text_var_key)]) - 65
        shift_more = (first_conv + shift) % 26
        code_back = chr(shift_more + 65)
        empty_str = empty_str + code_back


    # result message
    res_message = Text(Point(200, 225), "Resulting message: " + empty_str)
    res_message.draw(win)

    # click to close message
    close_mes = Text(Point(200, 380), "Click anywhere to Close Window")
    close_mes.draw(win)
    win.getMouse()
    win.close()
if __name__ == '__main__':
    vigenere()










