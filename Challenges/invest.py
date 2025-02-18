pa = float(input("Enter the principle ammount: "))
rate = float(input("Enter the rate of interest: "))
years = int(input("Enter the years of interest: "))

# Calculating the simple interest
amt = pa
for i in range(1, years+1):
    amt += (amt * rate)
    print(f"Total ammount after {years} years: ${amt}")