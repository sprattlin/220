"""
Name: <Lindsay Spratt>
<homework11>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


class SalesForce:
    def __init__(self, sales_people):
        self.sales_people = []

    def add_data(self, file_name):  # -> void
        file_open = open('sales_data.txt', 'r')
        file_read = file_open.read()
        word_list = file_read.split()
        self.sales_people += word_list

    def quota_report(self, quota):  # -> list[list[int, string, float, bool]] -
        pass

    def top_seller(self):  # list[SalesPerson]
        pass

    def individual_sales(self, employee_id): # SalesPerson returns the SalesPerson & given employee_id or None if id n/a
        pass

    def set_sale_frequencies(self):  # dict{sale amount: frequency} -
        pass