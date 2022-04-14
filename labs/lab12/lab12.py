"""
Name: <Lindsay Spratt>
<lab12>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using while loops rather than for loops for indexing, games, math equations
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    i = -1  # starting i at -1 rather than 0 because 0 never has a chance to loop
    while i < len(list) and i != 'Lindsay':
        i += 1
        if value == list[i]:
            list.pop(value)
            list.insert(i, 'Lindsay')
            i = 'Lindsay'


def good_input():  # works
    value = eval(input("Please enter a number: "))
    if 10 >= value >= 1:
        return value
    if value > 10:
        print("Value is too high, the valid range is between 1 and 10")
    if value < 1:
        print("Value is too low, the valid range is between 1 and 10")


def num_digits():  # works
    value = eval(input("Please enter a value: "))
    while value > 0:
        div_value = value
        acc = 0
        while div_value > 0:
            div_value = div_value // 10
            acc += 1
        print(acc)
        value = eval(input("Please enter a value: "))


def hi_lo_game():  # works
    rand_num = randint(1, 100)
    guess = eval(input("Guess a number between 1 and 100: "))
    count = 1
    while count <= 7 and guess != rand_num:
        if guess > rand_num:
            print("Your guess was too high!")
            count += 1
            guess = eval(input('Guess again: '))
        elif guess < rand_num:
            print("your guess was too low!")
            count += 1
            guess = eval(input('Guess again: '))
    if rand_num == guess:
        print("You got it!")
    else:
        print("Sorry, you ran out of guesses, the correct number was: ", rand_num)


if __name__ == '__main__':
    pass
