"""
Conditional statements and loops.

Demonstration:
- Using if / elif / else for decision making
- Iterating with a for loop using range
"""

temperature = 15

if temperature > 30:
    print("Warm")
elif temperature > 20:
    print("Nice")
else:
    print("Cold")


for i in range(3):
    print("Attempt", i)


"""
Output:
Cold
Attempt 0
Attempt 1
Attempt 2
"""
