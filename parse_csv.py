import csv

csv_file = open('attendees1.csv', 'r')

csv_reader =csv.DictReader(csv_file)

# for line in csv_reader:
#     print(line['email'])

new_file = open('new_names.csv', 'w')
fieldnames = ['first_name', 'last_name', 'email']
csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

csv_writer.writeheader()

for line in csv_reader:
    csv_writer.writerow(line)


csv_file.close()