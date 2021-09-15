import csv

f = open('people.csv', 'a', newline='')

tup1= ("stacey", 34)
writer = csv.writer(f)
writer.writerow(tup1)

f.close()