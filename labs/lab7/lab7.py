"""
Name: <Lindsay Spratt>
<lab7>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating weighted average/grades using if statements, for loops and reading and writing on files
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
def weighted_average(in_file_name, out_file_name):
    open_grades = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    read_grades = open_grades.readlines()
    student_count = 0
    for i in read_grades:
        student_av = 0
        student_weight_total = 0
        separate_line = i.split(':')
        name_ele = separate_line[0]
        grade_elements = separate_line[1]
        grade_elements = grade_elements.split()
        for x in range(0, len(grade_elements), 2):
            weights = eval(grade_elements[x])
            grades = eval(grade_elements[x + 1])
            student_av = (grades * weights + student_av) / 100
            student_weight_total += weights
        if student_weight_total < 100:
            out_file.write(name_ele + "'s " + "average: " + "Error: the weights are less than 100")
        elif student_weight_total > 100:
            out_file.write(name_ele + "'s " + "average: " + "Error: the weights are more than 100")
        else:
            student_count += 1
            class_average += student_av
            class_average = class_average // student_count
            out_file.write(name_ele + "'s " + "average: " + student_av)
    out_file.write(("Class average:  {:0>2}".format(class_average)
    open_grades.close()
    out_file.close()

if __name__ == '__main__':
    weighted_average('grades.txt', 'out_file_name')