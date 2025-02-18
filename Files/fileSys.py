from pathlib import Path

# Making new directories
cwd = Path.cwd()

# Make New Directory
new_dir = cwd / "TestingDir"

# If it already exists
new_dir.mkdir(exist_ok=True)

# Check if new dir exists
print(f"New Dir? : {new_dir.exists()}")
print(f"Is it a Dir? : {new_dir.is_dir()}")

# Try creating it again
new_dir.mkdir(exist_ok=True)
print("Set the exist_ok to be True.")

# With parent directory
path = cwd / "Parent" / "Child"
path.mkdir(parents=True, exist_ok=True)

# Create files using touch
filePath = path / 'demo.txt'
filePath.touch()
print(filePath.exists())
