# This script focuses on writing a function to convert temperature values from celsius to fahrenheit and vice versa.
def celcius_to_fahrenheit(degrees):
    return degrees * 9/5 + 32

def fahrenheit_to_celcius(degrees):
    return (degrees - 32) * 5/9

# Testing the function

print(celcius_to_fahrenheit(30))  # Should print 86
print(fahrenheit_to_celcius(86))  # Should print 30

# Working on user input
temp = float(input("Enter temperation in degrees F: "))
deg_c = fahrenheit_to_celcius(temp)
print(f"{temp} degrees Fahrenheit is = {deg_c} degrees")

temp = float(input("Enter temperation in degrees C: "))
deg_f = celcius_to_fahrenheit(temp)
print(f"{temp} degrees Celsius is = {deg_f} degrees")