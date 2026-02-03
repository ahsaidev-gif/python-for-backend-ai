"""
Function definitions and argument handling.

Demonstration:
- Defining reusable functions
- Returning values from functions
- Using *args to accept multiple inputs
- Iterating over arguments to perform aggregation
"""


def greet(name):
    return f"Hi {name}"


def multiply(*numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


# Function calls
print(greet("Akash"))
print(multiply(2, 3, 4))


"""
Output:
Hi Akash
24
"""
