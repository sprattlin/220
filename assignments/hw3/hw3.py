"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    value_count = eval(input("How many grades will you enter: "))    # variable input
    acc = 0
    for i in range(value_count):
        values = eval(input("Please enter your values: "))
        for x in range(int(values)):         # second loop is not working corectly, check variables
            acc = acc + (values + values)     # sum
            grade_average = acc/value_count      # average
    print("Your average is", grade_average)

def tip_jar():
    tip_amount = eval(input("How much would you like to donate?: "))
    acc = 0
    for i in range(tip_amount, 5):
       acc = sum((for i in range(tip_amount, 5)))




def newton():
    pass


def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    average()
