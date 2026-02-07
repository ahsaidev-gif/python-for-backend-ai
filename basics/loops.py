"""
Control flow examples using for loops, while loops, and related patterns.

Demonstrates:
- Iterating over strings, lists, and ranges
- Aggregation using loops
- State-based execution with while loops
- break and continue usage
- match statement
- Variable arguments and lambda usage
"""


# =========================
# FOR LOOP EXAMPLES
# =========================

for character in "Python":
    print(character)

names = ["Mosh", "John", "Sarah"]
for name in names:
    print(name)

for number in range(10):
    print(number)

prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print(f"Total: {total_price}")

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

counter = 1
while counter <= 5:
    print("*" * counter)
    counter += 1
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

user_input = int(input("Enter a number: "))

if user_input < 0:
    print("Negative")
elif user_input == 0:
    print("Zero")
else:
    print("Positive")


"""
Sample Output:
Enter a number: 5
Positive
"""


for number in range(2, 10):
    if number % 2 == 0:
        continue
    print(f"Odd number: {number}")


"""
Output:
Odd number: 3
Odd number: 5
Odd number: 7
Odd number: 9
"""


for candidate in range(2, 10):
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            break
    else:
        print(f"{candidate} is prime")


"""
Output:
2 is prime
3 is prime
5 is prime
7 is prime
"""


def http_error(status_code):
    match status_code:
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


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))


"""
Output:
earth/mars/venus
"""


items = [(1, "one"), (2, "two"), (3, "three")]
items.sort(key=lambda pair: pair[1])
print(items)


"""
Output:
[(1, 'one'), (3, 'three'), (2, 'two')]
"""
