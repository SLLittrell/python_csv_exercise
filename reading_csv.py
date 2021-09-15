import csv

csv_file = open('attendees1.csv')

csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0

for row in csv_reader:
    if line_count == 0:
        print(f'Column names are {",".join(row)}')
        line_count +=1
        
    else:
        print(f'yay')
        line_count +=1

print(f'processed {line_count}')

csv_file.close()