"""
Name: <Lindsay Spratt>
<homework11>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating classes for employee data
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work, but I discussed it with Ashley Woods
"""

from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):  # -> void
        file_open = open(file_name, 'r')
        file_read = file_open.read()
        word_list = file_read.split('\n')
        for i in range(len(word_list)):  # line is holding an integer
            current_line = word_list[i]
            current_line = current_line.split(', ')
            id = current_line[0]
            name = current_line[1]
            # now make a salesperson object
            person = SalesPerson(id, name)
            sales = current_line[2].split()
            for individual in sales:
                sale = float(individual)
                person.enter_sale(sale)
            self.sales_people.append(person)
        # each line of text in the file can become salesperson objects

    def quota_report(self, quota):  # -> list[list[int, string, float, bool]] -
        report = []
        for person in self.sales_people:
            person_list = []
            check_id = person.get_id()
            check_name = person.get_name()
            check_sales = person.total_sales()
            check_quota = person.met_quota(quota)
            person_list.append(check_id)
            person_list.append(check_name)
            person_list.append(check_sales)
            person_list.append(check_quota)
            report.append(person_list)
        return report

    def top_seller(self):  # list[SalesPerson]
        seller_list = []
        top_sales = []
        for sales in self.sales_people:
            profit = sales.get_sales()
            profit.sort()
            highest_sale = profit[-1]
            top_sales.append(highest_sale)
            top_sales.sort()
        if top_sales[-1] in top_sales[-2]:
            for i in self.sales_people:
                if top_sales[-1] in i.get_sales():
                    seller_list.append(i)
                    return seller_list
        elif top_sales[-1] == top_sales[-2]:
            for i in self.sales_people:
                if top_sales[-1] in i.get_sales():
                    seller_list.append(i)
                if top_sales[-2] in i.get_sales():
                    seller_list.append(i)
                    return seller_list

    def individual_sales(self,
                         employee_id):  # SalesPerson returns the SalesPerson & given employee_id or None if id n/a
        for i in self.sales_people:
            if employee_id == i.get_id():
                return 1

    def get_sale_frequencies(self):  # dict{sale amount: frequency} -
        sales_list = []
        for i in self.sales_people:
            sales = i.get_sales()
            sales_list.append(sales)
        frequency = {}
        for occurrence in sales_list:
            for item in occurrence:
                if item in frequency:
                    frequency[item] += 1
                else:
                    frequency[item] = 1
        return frequency
