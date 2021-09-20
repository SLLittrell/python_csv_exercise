import csv

# opens csv file with context manager
# 'a'= appends a new line to file and sets newline default to empty string
with open('csv_files/people.csv', 'a', newline='') as f:
# assigning newline content with a tuple to a var
    tup1= ("Stacey", 34)
# use writer method on opened csv file and assigning to var
    writer = csv.writer(f)
# writing a row to csv file and populating with tuple
    writer.writerow(tup1)

