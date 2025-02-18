phrase = "THis marks the spot"
for character in phrase:
    if character=="X":
        break
else:
    print("X is not in phrase!")


phrase = "THis marks the spot"
if "X" in phrase:
    print("Spot find.")
else:
    print("X is not in phrase!")
