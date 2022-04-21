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


def is_in_binary(search_val, values):
    left_index = 0
    right_index = len(search_val) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = search_val[middle_index]
        if middle_value == values:
            return middle_index
        elif middle_value < values:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
        return -1


def selection_sort(values):  # list of values
    for i in range(len(values)):
        pos_holder = i
        number = values[i]
        for j in range(i + 1, len(values)):
            if values[j] < number:
                number = values[j]
                pos_holder = j
        values[i], values[pos_holder] = values[pos_holder], values[i]


def calc_area(rect):
    get_point1 = rect.getP1()
    get_point2 = rect.getP1()
    x1 = get_point1.getX()
    y1 = get_point1.getY()
    x2 = get_point2.getX()
    y2 = get_point2.getY()
    y_dist = abs(y2) - abs(y1)
    x_dist = abs(x2) - abs(x1)
    area = y_dist * x_dist
    return area


def rect_sort(rectangles):  # list of graphic rectangles objects
    for i in range(len(rectangles)):
        pos_holder = i
        area = calc_area(rectangles[i])
        for j in range(i + 1, len(rectangles)):
            if calc_area(rectangles[j]) < area:
                area = calc_area(rectangles[j])
                pos_holder = j
        rectangles[i], rectangles[pos_holder] = rectangles[pos_holder], rectangles[i]







