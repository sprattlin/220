"""
Name: <Lindsay Spratt>
<homework11>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating classes for employee data
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work, but I discussed it with Ashley Woods
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):  # int- returns the sales person’s employee_id
        return self.employee_id

    def get_name(self):  # string - returns the sales person’s name
        return self.name

    def set_name(self, name):  # void - sets the sales person’s name
        self.name = name

    def enter_sale(self, sale):  # void - adds the value of sale to the sales list
        self.sales.append(sale)

    def total_sales(self):   # returns the sum of the sales person’s sales
        return sum(self.sales)

    def get_sales(self):  # list[float] - returns the list of sales
        return self.sales

    def met_quota(self, quota):  # boolean - returns True if the total sales meet or exceed the quota provided
        if quota >= self.total_sales():
            return True
        else:
            return False

    def compare_to(self, other):  # -> int
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        else:
            return 0

    def __str__(self):  # same format as constructor  returns “<employee_id>-<name>: <total sales>”
        return str(self.get_id()) + "-" + self.get_name() + ': ' + str(self.total_sales())




