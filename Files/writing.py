file_path = './sample2.txt'

# Write data to a file
with open(file_path, mode='w') as f:
    f.write('Hello Kitty!\n')

# Append data to a file
with open(file_path, mode='a') as f:
    f.write('Hello World!\n')

# Writing Lines
lines = ['Hello!\n', 'Hello Mr.?\n', 'Hello Mrs.?\n']
with open(file_path, mode='a') as f:
    f.writelines(lines)

# Read data
with open(file_path, mode='r') as f:
    print(f.read())
