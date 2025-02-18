# This script tries to explain a function's anatomy.
def mul(a, b): # Function's Signature
    
    # Function's Documentation
    """This function multiplies two numbers together.
    Parameters:
    a (int or float): The first number
    b (int or float): The second number
    Returns:
    int or float: The product of a and b
    """
    
    # Function's Body
    return a * b

def greet(name):
    """This function greets a person by name.
    Parameters:
    name (str): The person's name
    Returns:
    str: A greeting message
    """
    print(f"Hello, {name}!")
    # No return value
    
def cube(num):
    """This function calculates the cube of a number.
    Parameters:
    num (int or float): The number whose cube needs to be calculated
    Returns:
    int or float: The cube of num
    """
    return num ** 3

if __name__ == '__main__':
    print(mul(5, 6)) # Function's Call
    greet("John") # Function's Call
    print(greet("Yug"))