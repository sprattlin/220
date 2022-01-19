""""
Name: Lindsay Spratt
<lab1.py>

Problem: Writing a program to compute the monthly interest charge on a credit card account
Certification of Authenticty: I certify this assignment is my own work
"""
def monthly_interest():
    annual_interest = eval(input("Please enter your annual Interest rate: "))
    billing_cycle = eval(input("please enter the number of days in your billing cycle: "))
    previous_balance = eval(input("Please enter your previous net balance: "))
    payment_amount = eval(input("Please enter the payment amount: "))
    day_cycle = eval(input("Please enter the day of cycle your payment was made: "))
    step_1 = billing_cycle * previous_balance
    step_2 = payment_amount * (billing_cycle - day_cycle)
    step_3 = step_1 - step_2
    average_daily_balance = step_3/billing_cycle
    monthly_interest_rate = annual_interest/12
    monthly_interest_decimial = monthly_interest_rate/100
    monthly_interest = average_daily_balance * monthly_interest_decimial
    print("Your monthly interest rate is", "$", monthly_interest)

monthly_interest()









