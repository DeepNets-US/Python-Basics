temperature_readings = [68, 65, 68, 70, 74, 72]
filepath = './temperatures.txt'

with open(filepath, mode='w') as f:
    f.write(','.join(str(temp) for temp in temperature_readings))

with open(filepath, mode='r') as f:
    data = f.read().split(',')
    print(data)
