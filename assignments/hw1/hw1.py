"""
Name: <Lindsay Spratt>
<hw1>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
This program solves math equations in everyday life and is able to interpret a wide variety of variables.
Certification of Authenticity:
<I certify this assignment is my own work, but I discussed it with: Maeve O'toole>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("enter the Length: "))
    width = eval(input("enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("volume = ", volume)

def shooting_percentage():
    shots = eval(input("enter total shots: "))
    shots_made = eval(input("enter shots made: "))
    shooting_percentage = (shots_made / shots) * 100
    print("shooting_percentage = ", shooting_percentage)

def coffee():
    pounds_coffee = eval(input("How many pounds of coffee would you like? : "))
    cost = (0.86 * (10.50 * pounds_coffee)) + 1.5
    print("Your total amount is $", cost)

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you drive?: "))
    miles = (kilometers * 0.6214)
    print("You travelled", miles, "miles")

def main():
    calc_rec_area()
    calc_volume()
    shooting_percentage()
    coffee()
    kilometers_to_miles()
main()

