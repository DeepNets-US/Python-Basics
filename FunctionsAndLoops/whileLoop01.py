# This script explores the concept of when we need the while loop to run indefinitely

num = int(input("Enter a positive number: "))
while num <= 0:
    print("The number is not positive!")
    print("Please enter a positive number")
    num = int(input("Enter a number: "))

print("The number is positive!")