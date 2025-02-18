file_path = "./sample.txt"

# Read entire data at once
with open(file_path, mode='r', encoding='utf-8') as file:
    data = file.read()
print(data)


with open(file_path, mode='r', encoding='utf-8') as file:
    for line in file.readline():
        print(line)
