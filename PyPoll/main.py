import os
import csv

data1 = os.path.join("raw_data", "election_data_1.csv")
data2 = os.path.join("raw_data", "election_data_2.csv")

total = 0
C1 = "Vestal"
C2 = "Seth"
C3 = "Torres" 
C4 = "Cordin"

T1 = 0
T2 = 0
T3 = 0
T4 = 0

with open(data1, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader, None)


	for row in csvreader:
		total = total +1
		if row[2] == C1:
			T1 = T1 + 1
		elif row[2] == C2:
			T2 = T2 +1
		elif row[2] == C3:
			T3 = T3 +1
		elif row[2] == C4:
			T4 = T4 +1


