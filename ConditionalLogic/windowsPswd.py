for i in range(3):
    pswd = input("Enter Password: ")
    if pswd=="2569":
        break
    print(f"Incorrect Password, {3 - (i+1)} turns left!")
else:
    print("SUspicious activity, did you forget your password?")

