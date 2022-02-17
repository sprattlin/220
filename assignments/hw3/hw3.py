"""
Name: <Lindsay Spratt>
<hw3>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Running loops and sequences to solve everyday problems or advanced math.
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

def average():
    pass
    value_count = eval(input("How many grades will you enter: "))    # variable input
    acc = 0
    for grabbing_values in range(1, value_count + 1):
        grade = eval(input("Please enter your values: "))
        acc = acc + grade      # sum
    grade_average = acc / value_count       # averaging values outside of loop
    print("Your average is", grade_average)

def tip_jar():
    pass
    acc = 0     # accumulator to add tips together
    for entering_tips in range(5):      # range(5) because the bowl is being passed to exactly 5 people
        tip_amount = eval(input("How much would you like to donate?: "))
        acc = acc + tip_amount
    print("Total tips: $", acc)

def newton():
    pass
    number_input = eval(input("What number do you want to square root? "))      # no acc because the user tells you how many times you want to refine
    approximation_input = eval(input("How many times should we improve the approximation?  ")) # not accumulating any values
    approx = number_input / 2
    for run_approx in range(approximation_input):        # in range of approximation input bc user tells us how many times to run
        approx = (approx + (number_input/approx)) / 2
    print(approx)

def sequence():
    pass
    sequence_input = eval(input("How many terms would you like?"))
    for series in range(1, sequence_input, + 1):    # + 1 at then end because stops are non-inclusive
        sequence_start = (series + 1) % 2
    print(series + sequence_start)

def pi():
    n = eval(input("Please enter how many terms are in the series: "))
    acc = 1   # acc 1 because multiplication
    for i in range(n):
       rightform = i + (2.0 - (i % 2.0))    # mod - remainder
       leftform = i + (1.0 + (i % 2.0))
       acc = acc * (rightform/leftform)
    pi = acc * 2
    print(pi)
if __name__ == '__main__':
    average()
    tip_jar()
    newton()
    sequence()
    pi()