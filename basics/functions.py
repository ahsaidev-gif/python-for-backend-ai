"""
Function definitions and argument handling.
"""


def greet(name):
    return f"Hi {name}"


def multiply(*numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


print(greet("Akash"))
print(multiply(2, 3, 4))
