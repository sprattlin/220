"""
Name: <your name goes here – first and last>
<hw6>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Writing code with formatting, parameters, arguments and creating ciphers
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import math
def cash_converter():
    cash = eval(input("Please enter an integer: "))
    print("That is ${:.2f}".format(cash))

def encode():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    for i in range(len(message)):
        first_conv = ord(message[i])
        x = first_conv + int(key)
        convert_back = chr(x)
        print(convert_back, end="")

def sphere_area(radius):
    # radius = eval(input("Please enter the float value of the radius: "))
    area = (4.0 * math.pi * (radius**2))
    return area

def sphere_volume(radius):
    # radius = eval(input("Please enter the float value of the radius: "))
    volume = (4.0/3.0) * math.pi * (radius**3)
    return volume

def sum_n(number):
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum(number)
    return result

def sum_n_cubes(number):
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared = [number ** 2]
    result = sum(squared)
    return result


def encode_better():
    message = input("Please enter a message: ")
    key = input("Please enter a key: ")
    empty_str = ''
    for i in range(len(message)):
        conv_mes = ord(message[i]) - 65
        conv_key = ord(key[i % len(key)]) - 65
        shift = (conv_mes + conv_key) % 58
        cipher = shift + 65
        cipher_conv = chr(cipher)
        empty_str += cipher_conv
    print(empty_str)

if __name__ == '__main__':
    cash_converter()
    encode()
    res = sphere_area(13)
    print(res)
    res = sphere_volume(13)
    print(res)
    res = sum_n(100)
    print(res)
    res = sum_n_cubes(13)
    print(res)
    encode_better()

