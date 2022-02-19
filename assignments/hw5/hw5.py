"""
Name: <Lindsay Spratt>
<hw5>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using slicing, indexing, and format function to access parts of lists
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    f, l = input("Please enter your name: ").split()
    print(l + ", " + f)

def company_name():
    company = input("Please enter a three-part internet domain: ")
    domain = company.split(".")[1]
    print(domain)

def initials():
    students = eval(input("How many students are in the class? "))
    acc = 0
    for i in range(0, students):
        acc = acc + 1
        x = input("What is the name of student {}? ".format(acc))
        f,l = x.split()
        print(f[0] + l[0])
def names():
    name_list = input("Please enter a list of names: ")
    splice = name_list.split(' ')
    sep = " "
    for i in splice:
        sep += i[0]
    print(sep)

def thirds():
    n = eval(input("Please enter the number of sentences: "))
    for i in range(1, n +1):
        sentence = input("Enter sentence " + str(i) + "here")
        print(sentence[2::3])
def word_average():
    sen = (input("Please enter a sentence you wish to average: "))
    sen = sen.split()
    acc = 0
    for word in sen:
        acc = acc + len(word)
    print(acc / len(sen))

def pig_latin():
    sentence = input("Enter the sentence: ")
    words = sentence.split()
    new_sentence = ""
    for w in words:
        new_sentence += w[1:] + w[0] + "ay "
    print(new_sentence.lower())

if __name__ == '__main__':
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
