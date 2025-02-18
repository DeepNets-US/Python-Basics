from pathlib import Path

# Specify a file path
og_file_path = Path.cwd() / "TestingDir" / "Parent" / "names_6.txt"

# Check if path exists
# print(og_file_path.exists())

# Get the new location
new_file_path = Path.cwd() / "TestingDir" / "names_6.txt"

# Try Moving
og_file_path.replace(new_file_path)
