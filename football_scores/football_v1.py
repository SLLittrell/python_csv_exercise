import csv

with open('football_stats.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
           differential = abs(int(row['Goals For']) - int(row['Goals Against']))
           print(f'{row["Team"]} score differential was {differential}')
           