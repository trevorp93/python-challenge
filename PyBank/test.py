import os
import csv

data1 = os.path.join("raw_data", "budget_data_1.csv")
data2 = os.path.join("raw_data", "budget_data_2.csv")

months = 0
revenue = 0
high = 0
low = 0

with open(data1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        print(row[0])