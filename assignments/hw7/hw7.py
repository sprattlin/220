"""
Name: <Lindsay Spratt>
<hw7>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
manipulating files and string comprehension
Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Ashley Woods>
"""
import math

def number_words(in_file_name, out_file_name):
    open_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    text = open_file.read()
    text.split()
    for i in range(1, len(text), 1):
        loop = text[i]
        string_create = eval(loop) + (1, ":", text)
        conv_add = str(string_create)
        out_file.write(conv_add)
    open_file.close()
    out_file.close()
def hourly_wages(in_file_name , out_file_name):
    open_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    text = open_file.readlines()
    for i in range(len(text)):
        separate = text[i]
        separate = separate.split()
        bonus = eval(separate[2]) + 1.65
        week_pay = eval(separate[3]) * bonus
        out_file.write("{} {:.2f}\n".format(separate[0] + ' ' + separate[1], week_pay)) # one employee per line
    open_file.close()
    out_file.close()
def calc_check_sum(isbn):
    isbn_new = isbn.replace("-", "")
    if len(isbn_new) != 10:
        print("Typing error")
        exit(0)
    isbn_number = int(isbn_new)
    check_sum_result = 0
    index = 1
    while isbn_number != 0:
        check_sum_result += (isbn_number % 10) * index
        isbn_number = math.floor(isbn_number / 10)
        index += 1
    return check_sum_result
def send_message(file_name, friend_name):
    file_open = open(file_name, "r")
    friend = open(friend_name + '.txt', "w")
    friend_string = (friend.read())
    new_name = file_open.write(friend_string)
    print(new_name)
    file_open.close()
    friend.close()
def send_safe_message(file_name, friend_name, key):
    from encryption import encode
    open_file = open(file_name, "r")
    open_friend = open(friend_name, "w")
    message = open_file.readline()
    separate = message.split('\n')
    for i in range(len(separate)):
        first_conv = ord(separate[i])
        x = first_conv + int(key)
        convert_back = chr(x)
        convert_back.rstrip()
        print(convert_back, end="")
    open_file.close()
    open_friend.close()
def send_uncrackable_message(file_name, friend_name, pad_file_name):
    from encryption import encode_better
    open_file = open(file_name, "r")
    message = open_file.readlines()
    pad_file_open = open(pad_file_name, "r")
    pad_file = pad_file_open.readlines()
    out_file = open(friend_name, "w")
    out_file.readlines()
    empty_str = ''
    for i in range(len(message)):
        conv_mes = ord(message[i]) - 65
        expand_1 = str(pad_file)
        conv_key = ord(expand_1[i % len(pad_file)]) - 65    #
        shift = (conv_mes + conv_key) % 58
        cipher = shift + 65
        cipher_conv = chr(cipher)
        empty_str += cipher_conv
    out_file.write(friend_name + ".txt")
    open_file.close()
    pad_file_open.close()
    out_file.close()

if __name__ == '__main__':
    number_words("hourly_wages.txt", "out_file")
    hourly_wages("hourly_wages.txt", "out_file")
    res = calc_check_sum("0-072-94652-0")
    send_message('message', 'bob.txt')
    send_safe_message("secret_message", 'bob.txt', 2)
    send_uncrackable_message("super_secret_message", "bob.txt", 'pad.txt')





