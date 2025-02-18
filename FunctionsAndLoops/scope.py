# Code 01
x = "Hello, world!"


def func():
    x = 2
    print(f"The value of x inside the function is : {x}")


func()
print(f"The value of x outside the function is : {x}")

# Code 02
x = 3


def outer_func():
    y = 3

    def inner_func():
        return x + y
    return inner_func()


print(outer_func())

# Code 03
total = 0


def add_to_total(n):
    global total # The Fix
    total = total + n


add_to_total(5)
print(total)
