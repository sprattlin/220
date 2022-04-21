"""
Name: <Lindsay Spratt>
<lab13>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Using algorithms to extract data from parameters and use in real-world situations
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work
"""


def trade_alert(filename):
    open_file = open(filename, 'r')
    read_file = open_file.readline()
    stock_list = read_file.split()
    for i in range(len(stock_list)):
        if eval(stock_list[i]) > 830:
            seconds = i + 1
            print("Warning! at this time of ", seconds, " seconds the trading volume has exceeded a volume of 830")
        elif eval(stock_list[i]) == 500:
            seconds = i + 1
            print("Pay attention! Currently at ", seconds, "seconds the trading volume is 500")
    open_file.close()


trade_alert('trades.txt')

