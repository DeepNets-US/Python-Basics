while True:
    sent = input("Enter any string: ")
    bound = input("Enter an Index: ")

    try:
        bound = int(bound)
    except ValueError:
        print("The index should be an Integer.\n")
        continue
    
    if not 0<=bound<len(sent):
        print("The index is out of bound.\n")
        continue

    print(f"Output: {sent[bound]}")
