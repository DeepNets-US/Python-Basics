# This file is an introduction to "break" & "continue"  keyword in Python.
for i in range(5):
    if i==2:
        break
    print(f"Value of i is {i}")

for i in range(5):
    if i==2:
        continue
    print(i) # This should skip 2 and work for the rest


