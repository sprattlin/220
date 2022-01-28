"""
Name: <Lindsay Spratt>
<hw2>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Manually creating code that either uses the import math functions or creates it's own functions without the help of
pre-existing math modules to output the results of mathematical equations that are susceptible to any variable.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <w3schools.com, datacamp.com>
"""
import math

def sum_of_threes():
    acc = 0
    y = eval(input("What is the upper bound? "))
    for i in range(0, y + 1, 3):        # loop start
        acc = acc + i
    print(acc)

def multiplication_table():  # use range type
    for l in range(1, 11):         # height X length and end number + 1
        for h in range(1, 11):
            print((h * l), end=" ")
        print()

def triangle_area():
    side_1 = eval(input("Please enter the length of the first side of the triangle: "))       # variable input number 1
    side_2 = eval(input("Please enter the length of the second side of the triangle: "))      # variable input number 2
    side_3 = eval(input("Please enter the length of the final side of the triangle: "))        # last variable input
    s = (side_1 + side_2 + side_3)/2
    a = math.sqrt(s*(s-side_1)*(s - side_2)*(s - side_3))
    print(a)

def sum_squares():
    lower_range = eval(input("Please enter your lower range value: "))      # variable input 1
    upper_range = eval(input("Please enter your upper range value: "))      # variable input 2
    acc = 0         # loop start
    for i in range(lower_range, upper_range + 1):           # running loop on upper & lower values
        acc = acc + (i * i)             # finding the sum
    print(acc)

def power():
    base_val = eval(input("Please enter your base value: "))    # base variable input
    exponent_val = eval(input("Please enter your exponent value: "))    # exponent variable input
    acc = 1         # acc of 1 because multiplication
    for x in range(exponent_val):       # creating loop
        acc = acc * base_val        # this is manually creating the exponent output
    print(base_val, "^", exponent_val, "=", acc)       # printing output

if __name__ == '__main__':
    sum_of_threes()
    multiplication_table()
    triangle_area()
    sum_squares()
    power()