import csv
daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
]

# Writing using csv
with open('dailytemps.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(daily_temperatures)

# Reading using csv
with open('dailytemps.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
