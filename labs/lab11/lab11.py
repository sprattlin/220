"""
Name: <Lindsay Spratt>
<lab11>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating three door simulation
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from lab10.button import Button
from lab10.door import Door
from random import randint


def main():
    # creating window
    win = GraphWin("Three Door Game", 800, 800)
    win.setBackground("light blue")

    # creating score-keeper
    wins_box = Rectangle(Point(50, 30), Point(100, 80))
    win_acc = 0
    wins = Text(Point(75, 55), win_acc).draw(win)
    loss_box = Rectangle(Point(100, 30), Point(150, 80))
    loss_acc = 0
    losses = Text(Point(125, 55), loss_acc).draw(win)
    Text(Point(75, 20), 'wins').draw(win)
    Text(Point(125, 20), 'losses').draw(win)
    wins_box.draw(win)
    loss_box.draw(win)

    # messages
    secret_message = Text(Point(400, 80), "I have a secret door")
    guess_message = Text(Point(400, 730), "Click to guess which is the secret door!")
    secret_message.draw(win)
    guess_message.draw(win)

    # button create & draw
    button_create = Button(Rectangle(Point(650, 30), Point(750, 80)), 'Quit')
    button_create.draw(win)

    # doors create & draw
    door_1 = Door(Rectangle(Point(150, 250), Point(250, 550)), 'Door 1')
    door_2 = Door(Rectangle(Point(350, 250), Point(450, 550)), "Door 2")
    door_3 = Door(Rectangle(Point(550, 250), Point(650, 550)), "Door 3")
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)
    # doors color
    door_1.color_door('brown')
    door_2.color_door('brown')
    door_3.color_door('brown')
    door_list = [door_1, door_2, door_3]
    # wrong door
    wrong_door = Text(Point(400, 80), "Sorry wrong door")
    right_door = Text(Point(400, 80), "You guessed it!")
    # play again
    play_again = Text(Point(400, 730), "Click anywhere to play again")
    # setting up secret door
    point = win.getMouse()
    index = randint(0, 2)
    secret_door = door_list[index]
    # gameplay
    while not button_create.is_clicked(point):
        if not secret_door.is_clicked(point):
            secret_message.undraw()
            guess_message.undraw()
            loss_acc += 1
            secret_door.color_door('green')
            wrong_door.draw(win)  # already drawn
            play_again.draw(win)
        if secret_door.is_clicked(point):
            secret_message.undraw()
            guess_message.undraw()
            win_acc += 1
            secret_door.color_door('green')
            right_door.draw(win)  # already drawn
            play_again.draw(win)
    else:
        win.close()


main()
