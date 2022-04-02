"""
Name: <Lindsay Spratt>
<hw9>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating hangman game
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *


def get_words(file_name):
    open_file = open(file_name, "r")
    read_file = open_file.readlines()
    return read_file


def get_random_word(words):
    random_num = randint(0, len(words) - 1)  # int() argument must be a string, not list
    random_word = words[random_num]
    return random_word


def letter_in_secret_word(letter, secret_word):
    return letter in secret_word


def already_guessed(letter, guesses):
    return letter in guesses


def make_hidden_secret(secret_word, guesses):  # secret word : 'tree' STRING  guesses: ['a', 't', 'e']
    guessed = ''
    for characters in range(len(secret_word)):
        if secret_word[characters] in guesses:
            guessed += secret_word[characters] + ' '
        else:
            guessed += '_ '
    guessed = guessed.strip()
    return guessed
# if they guessed it, leave letter there, if they haven't guessed it, turn it into an underscore
# 'in <string>' requires string as left operand, not list


def won(guessed):  # guessed would be equal to the word if they won
    if '_' not in guessed:
        return True
    else:
        return False


def play_graphics(secret_word):  # create window
    win = GraphWin("Hangman", 1000, 1000)
    # stand up pole
    pole1 = Line(Point(500, 200), Point(500, 700))
    # base of pole
    pole2 = Line(Point(475, 700), Point(525, 700))
    # head of pole
    pole3 = Line(Point(475, 200), Point(525, 200))
    # hanging pole
    pole4 = Line(Point(475, 200), Point(475, 250))
    # draw
    pole1.draw(win)
    pole2.draw(win)
    pole3.draw(win)
    pole4.draw(win)
    # body of hangman
    head = Circle(Point(475, 250), 15)
    neck = Line(Point(475, 250), Point(475, 260))
    arm1 = Line(Point(475, 260), Point(450, 275))
    arm2 = Line(Point(475, 260), Point(500, 245))
    torso = Line(Point(475, 260), Point(475, 300))
    leg1 = Line(Point(475, 300), Point(450, 325))
    leg2 = Line(Point(475, 300), Point(500, 325))
    play_command_line(secret_word)
    body_list = [head, neck, arm1, arm2, torso, leg1, leg2]
    # for loop for guesses
    for i in range(1, 7, -1):
        text_box = Entry(Point(500, 750), 20)
        text_box_text = text_box.setText("Guesses")  # error function has no return
        text_box_text.draw(win)
        text_box.draw(win)
        guessed = text_box.getText()
        guessed_text = Text(Point(490, 500), "Guessed letters: ")
        guessed_text.draw(win)
        guessed_letters_text = Text(Point(500, 500), guessed)
        guessed_letters_text.draw(win)
        if guessed not in secret_word:
            for parts in body_list:
                index = body_list[parts]
                index.draw(win)


def play_command_line(secret_word):
    guessed = []
    guessed_right = make_hidden_secret(secret_word, guessed)
    guesses_remaining = 6
    while guesses_remaining >= 0 and not guessed_right == secret_word:
        print('already guessed: ', guessed, '\n', 'guesses left: ', guesses_remaining)
        print(guessed_right)
        player_guess = input("guess a letter: ")
        guessed.append(player_guess)
        if letter_in_secret_word(player_guess, secret_word):
            guessed_right = make_hidden_secret(secret_word, guessed)
        else:
            guesses_remaining = guesses_remaining - 1
        if guessed_right.split(' ') == list(secret_word):
            print('you won!', guessed_right)
            break
        elif guesses_remaining == 0:
            print('you did not guess the word', '\n', 'the secret word was: ', secret_word)
        else:
            print()


# while loop to make sure they didnt win
# while loop to make sure there are guesses left


if __name__ == '__main__':
    pass
