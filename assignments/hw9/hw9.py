"""
Name: <Lindsay Spratt>
<hw9>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating hangman game
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def get_words(file_name):
    open_file = open(file_name, "r")
    read_file = open_file.readlines()
    return read_file


def get_random_word(words):
    random_word = randint(words, len(get_words('words.txt')))  # int() argument must be a string, not list
    return random_word


def letter_in_secret_word(letter, secret_word):
    return letter in secret_word


def already_guessed(letter, guesses):
    return letter in guesses


def make_hidden_secret(secret_word, guesses):
    acc = ''
    for characters in secret_word:
        hidden = secret_word.replace(characters, ' _ ')
        acc += hidden
        if guesses in secret_word:
            show_letter = secret_word.replace(acc, guesses)
            show_letter.append(guesses)
            return show_letter
    #     acc += hidden
    #     return acc
    # if guesses in secret_word:
    #     show_letter = secret_word.replace(acc, guesses)  # missing first and last letter, and space in between
    #     return show_letter
#
# builtin_function_or_method object is not subscript able
# not getting all the letters needed
def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
