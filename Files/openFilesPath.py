from pathlib import Path

# Specify the file path
file_path = Path.cwd() / "sample.txt"

# open the file
file = file_path.open(mode="r", encoding='utf-8')

# Read Files
entire_data = file.read()
print(f"Reading entire file: {entire_data}")

# Read file line by line
print(file.readlines())

# Make sure to close the file
file.close()
