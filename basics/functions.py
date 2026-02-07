"""
Function definitions and argument handling.

Demonstrates:
- Defining reusable functions
- Returning values from functions
- Using *args to accept multiple inputs
- Iterating over arguments to perform aggregation
- range() usage
- Function arguments and best practices
"""

import sys


# =========================
# BASIC FUNCTIONS
# =========================

def greet(name):
    return f"Hi {name}"


def multiply(*numbers):
    total = 1
    for value in numbers:
        total *= value
    return total


print(greet("Akash"))
print(multiply(2, 3, 4))

"""
Output:
Hi Akash
24
"""


# =========================
# RANGE FUNCTION
# =========================

for number in range(5):
    print(number)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

"""
Output:
0
1
2
3
4
[5, 6, 7, 8, 9]
[0, 3, 6, 9]
[-10, -40, -70]
"""


# =========================
# RANGE WITH INDEX
# =========================

words = ["Mary", "had", "a", "little", "lamb"]

for index in range(len(words)):
    print(index, words[index])

"""
Output:
0 Mary
1 had
2 a
3 little
4 lamb
"""


# =========================
# FUNCTION: FIBONACCI (PRINT)
# =========================

def fib(limit):
    """Print Fibonacci numbers less than limit."""
    a, b = 0, 1
    while a < limit:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(50)

"""
Output:
0 1 1 2 3 5 8 13 21 34
"""


# =========================
# FUNCTION: FIBONACCI (RETURN)
# =========================

def fib_list(limit):
    """Return Fibonacci series less than limit as a list."""
    result = []
    a, b = 0, 1
    while a < limit:
        result.append(a)
        a, b = b, a + b
    return result


print(fib_list(50))

"""
Output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""


# =========================
# DEFAULT ARGUMENTS
# =========================

def greet_default(name="User"):
    print(f"Hello {name}")


greet_default()
greet_default("Akash")


# =========================
# MUTABLE DEFAULT PITFALL
# =========================

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item(1))
print(add_item(2))

"""
Output:
[1]
[2]
"""


# =========================
# *ARGS AND **KWARGS
# =========================

def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))


# =========================
# KEYWORD ARGUMENTS
# =========================

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")


# =========================
# POSITIONAL & KEYWORD ONLY
# =========================

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


combined_example(1, 2, kwd_only=3)


# =========================
# LAMBDA EXPRESSIONS
# =========================

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])

print(pairs)


# =========================
# DOCSTRINGS & ANNOTATIONS
# =========================

def format_message(text: str) -> str:
    """Return formatted message."""
    return f"[INFO] {text}"


print(format_message("Service started"))


# =========================
# DIR FUNCTION
# =========================

print(dir(sys))
