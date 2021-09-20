import csv

file = open('attendees1.csv')

attendees1 = []

csv_f = csv.reader(file)

for row in csv_f:
    attendees1.append(row[2])



file = open('attendees2.csv')

attendees2 = []

csv_f = csv.reader(file)

for row in csv_f:
    attendees2.append(row[2])


attendees1 = set(attendees1)
attendees2 = set(attendees2)

print(attendees2.difference(attendees1))

file.close()