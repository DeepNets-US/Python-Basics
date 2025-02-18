from pathlib import Path

# Specify Path
path = Path.cwd() / "TestingDir"

# Glob with *
print("Using *")
for p in path.glob("*"):
    print(p)

# Glob with ?
print("\nUsing ?")
for p in path.glob('names_?.txt'):
    print(p)

# Glob with []
print("\nUsing []")
for p in path.glob('names_[13].txt'):
    print(p)

# Glob with **
print("\nUsing **")
for p in path.glob('**/names_?.txt'):
    print(p)

# Glob with rglob
print("\nUsing rglob")
for p in path.rglob('names_?.txt'):
    print(p)

