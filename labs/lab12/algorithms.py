"""
Name: <Lindsay Spratt>
<lab12>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
reading and searching for data in a file using only while loops
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    file_open = open(filename, 'r')
    read_file = file_open.read()
    while read_file:
        file_list = read_file.split()
        return file_list
    file_open.close()


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False

