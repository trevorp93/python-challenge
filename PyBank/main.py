import os
import csv



data1 = os.path.join("raw_data", "budget_data_1.csv")
data2 = os.path.join("raw_data", "budget_data_2.csv")
result = os.path.join("result.txt")

months = 0
revenue = 0.00
high = 0
low = 0

with open(data1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        months = months + 1
        revenue = float(row[1]) + revenue
        if(float(row[1]) >= high):
        	high = float(row[1])
        	a = row[0]
        elif(float(row[1]) <= low):
        	low = float(row[1])
        	b = row[0]



with open(data2, newline="") as csvfile: 
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader, None)
	for row in csvreader:
		months = months +1
		revenue = float(row[1]) + revenue
		if(float(row[1]) >= high):
			high = float(row[1])
			a = row[0]
		elif(float(row[1]) <= low):
			low = float(row[1])
			b = row[0]



average = revenue/months

print("")
print("Financial Analysis")
print("----------------------------")
print("Total Months:", months)
print ("Total Revenue:","$"+'{0:.2f}'.format(revenue))
print("Average Revenue Change" ,"$"+'{0:.2f}'.format(average))
print("Greatest Increase in Revenue:",a,"("+"$"+'{0:.2f}'.format(high)+")")
print("Greatest Decrease in Revenue:",b,"("+"$"+'{0:.2f}'.format(low)+")")
print("")

textfile = open(result,"w")
textfile.write("Financial Analysis")
textfile.write("\n")
textfile.write("----------------------------")
textfile.write("\n")
textfile.write("Total Months: "+ str(months))
textfile.write("\n")

textfile.write("Total Revenue: $"+str('{0:.2f}'.format(revenue)))
textfile.write("\n")
textfile.write("Average Revenue Change $"+ str('{0:.2f}'.format(average)))
textfile.write("\n")
textfile.write("Greatest Increase in Revenue: " + a +" ("+"$"+str('{0:.2f}'.format(high))+")")
textfile.write("\n")
textfile.write("Greatest Decrease in Revenue: " + b + " ($" + str('{0:.2f}'.format(low)) + ")")
