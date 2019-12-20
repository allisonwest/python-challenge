import os
import csv
import numpy

csvpath = os.path.join('Data/budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    
    change_list = []
    greatest_increase = 0
    greatest_decrease = 0
    
    total = 0
    months = 0
    change = 0
    
    for row in csvreader:
        total += int(row[1])
        months += 1
        change = int(row[1]) - prev_net
        change_list = (change_list + [change])
        prev_net = int(row[1])


    change_array = numpy.array(change_list)
    change_min = numpy.min(change_array)
    change_max = numpy.max(change_array)
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${float(total)}")
    print(f"Average Change: ${sum(change_list)/len(change_list)}")  
    print(f"Greatest Increase: ${change_max}")
    print(f"Greatest Decrease: ${change_min}")