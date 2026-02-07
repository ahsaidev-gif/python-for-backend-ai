"""
Conditional statements and loops.

Demonstrates:
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


for attempt_number in range(3):
    print("Attempt", attempt_number)


"""
Output:
Cold
Attempt 0
Attempt 1
Attempt 2
"""
