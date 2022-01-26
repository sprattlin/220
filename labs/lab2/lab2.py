"""
Name: <Lindsay Spratt>
<lab2>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating code for arithmetic to be flexible with any variable and generate reliable outputs
Certification of Authenticity:
<I certify this assignment is my own work>
"""

def means():
    acc = 0 #rms accumulator
    hm_acc = 0  # start of harmonic mean formula
    gm_acc = 1 #geometric mean accumulator
    value_count = eval(input("Please enter how many values you wish to enter: "))
    for i in range(value_count):
        values = eval(input("Please enter your values: "))
        acc = acc + values**2  #root-mean-square formula start
        hm_acc = hm_acc + (1/values) #harmonic mean formula start
        gm_acc = (gm_acc * values) #geometric mean formula start
    gm_sqrt = gm_acc**(1/value_count)
    harmonic_mean_1 = value_count/hm_acc
    division = acc / value_count  # dividing values in first part of rms equation
    final_value_rms = division ** (1 / 2)  # squaring the values
    print("Here is your final value for root mean square:", final_value_rms)
    print("Here is your final value for harmonic mean: ", harmonic_mean_1)
    print("Here is your final value for geometric mean: ",gm_sqrt)
means()











