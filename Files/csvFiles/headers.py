import csv

# Specify file path
file_path = './temps.csv'

# Read the file
print('Normal CSV Reader:')
with open(file_path) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Reading using DictReader
print('\nDictReader: ')
with open(file_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
