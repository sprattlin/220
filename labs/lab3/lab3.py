"""
Name: <Lindsay Spratt>
<lab3>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Creating code for the sum and average of daily traffic
Certification of Authenticity:
<I certify this assignment is my own work>
"""
def traffic():
    roads_surveyed = eval(input("Please state how many roads were surveyed: "))
    acc = 0
    all_roads = 0 # accumulator for total num of vehicles, needs to be outside the loop to stop repeating
    for x in range(1, roads_surveyed + 1): # starting at 1 to make sure '0' doesn't print as an option, adding+1 at the end to now lose an input
        acc = acc + 1
        print("Please enter how many days road", x, "was surveyed: ", end='')  # using print to add more than one message
        days_surveyed = eval(input(" "))           # using eval(input now to convert the input to an int
        total_cars = 0
        for i in range(1, days_surveyed + 1):   # starting at 1 to make sure '0' doesn't print as an option, adding+1 at the end to now lose an input
            print("\tHow many cars travelled on day",i,"?: ", end='') # using variable i to see the loop of roads, i is the variable for day number/count
            cars_travelled = eval(input(" "))   # using eval to convert to int
            total_cars = cars_travelled + total_cars # average for vehicles per day
        all_roads = all_roads + total_cars # this accumulator will add together total vehicles travelled on all roads
        print("Road",x, "average vehicles per day is: ", total_cars/days_surveyed) # average vehicles per day
    print("Total number of vehicles on all roads is ", all_roads) # total number of vehicles on all roads
    print("Average number of vehicles per road is ", all_roads/x) # average number of vehicles per road

traffic()