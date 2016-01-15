import csv

with open('sleep_hours_per_day.csv', mode='r') as infile:
	reader = csv.reader(infile)
	for row in reader:
		print(row)


