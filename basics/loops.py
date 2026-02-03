"""
Control Flow Examples: for loops, while loops, and miscellaneous patterns.

Demonstration:
- Iterating over strings, lists, ranges
- Aggregation using loops
- State-based execution with while loops
- break / continue usage
- match statement
- Variable arguments and lambda usage
"""

# =========================
# FOR LOOP EXAMPLES
# =========================

# Iterating over a string
for char in "Python":
    print(char)

# Iterating over a list
names = ["Mosh", "John", "Sarah"]
for name in names:
    print(name)

# Iterating using range
for i in range(10):
    print(i)

# Aggregation example
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Enumerate example
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)


"""
Output (for loop section):
P
y
t
h
o
n
Mosh
John
Sarah
0
1
2
3
4
5
6
7
8
9
Total: 60
0 a
1 b
2 c
"""


# =========================
# WHILE LOOP EXAMPLES
# =========================

# Pattern printing
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")


"""
Output:
*
**
***
****
*****
Done
"""


# Guessing game
# Assumption: secret_number = 9
# Sample inputs: 3, 5, 9

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1

    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")


"""
Sample Output:
Guess: 3
Guess: 5
Guess: 9
You won!
"""


# Car game (command-driven loop)
# Sample inputs: help, start, stop, quit

started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started...")

    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")

    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to quit
""")

    elif command == "quit":
        break

    else:
        print("Sorry, I don't understand.")


"""
Sample Output:
> help
start - to start the car
stop  - to stop the car
quit  - to quit

> start
Car started...

> stop
Car stopped.

> quit
"""


# =========================
# MISC CONTROL FLOW
# =========================

# If / elif / else
# Sample input: 5

x = int(input("Enter a number: "))

if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")


"""
Sample Output:
Enter a number: 5
Positive
"""


# Loop control with continue
for num in range(2, 10):
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")


"""
Output:
Odd number: 3
Odd number: 5
Odd number: 7
Odd number: 9
"""


# Loop with else (prime check)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(f"{n} is prime")


"""
Output:
2 is prime
3 is prime
5 is prime
7 is prime
"""


# match statement (Python 3.10+)
def http_error(status):
    match status:
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Error"


print(http_error(404))
print(http_error(500))
print(http_error(403))


"""
Output:
Not Found
Server Error
Unknown Error
"""


# Function with variable arguments
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))


"""
Output:
earth/mars/venus
"""


# Lambda example
items = [(1, "one"), (2, "two"), (3, "three")]
items.sort(key=lambda item: item[1])
print(items)


"""
Output:
[(1, 'one'), (3, 'three'), (2, 'two')]
"""
