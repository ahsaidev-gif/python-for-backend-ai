"""
Conditionals and logical operations.
Demonstrates decision-making patterns used in backend systems.
"""

# =========================
# BASIC IF / ELIF / ELSE
# =========================

number = int(input("Please enter an integer: "))

if number < 0:
    number = 0
    print("Negative changed to zero")
elif number == 0:
    print("Zero")
elif number == 1:
    print("Single")
else:
    print("More")

"""
Sample Input:
42

Output:
More
"""


# =========================
# LOGICAL OPERATORS
# =========================

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
    print("Enjoy your day")

"""
Output:
It's a cold day
Wear warm clothes
"""


# =========================
# OR OPERATOR
# =========================

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

"""
Output:
Eligible for loan
"""


# =========================
# AND + NOT
# =========================

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

"""
Output:
Eligible for loan
"""


# =========================
# COMPARISON OPERATORS
# =========================

temperature = 35

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

"""
Output:
It's a hot day
"""


full_name = "John Smith"

if len(full_name) < 3:
    print("Name must be at least 3 characters")
elif len(full_name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")

"""
Output:
Name looks good!
"""


# =========================
# PROJECT: WEIGHT CONVERTER
# =========================

weight_value = int(input("Weight: "))
weight_unit = input("(L)bs or (K)g: ")

if weight_unit.upper() == "L":
    converted_weight = weight_value * 0.45
    print(f"You are {converted_weight} kilos")
else:
    converted_weight = weight_value / 0.45
    print(f"You are {converted_weight} pounds")

"""
Sample Input:
Weight: 160
(L)bs or (K)g: L

Output:
You are 72.0 kilos
"""


# =========================
# LOOP ELSE (PRIME CHECK)
# =========================

for number in range(2, 10):
    for divisor in range(2, number):
        if number % divisor == 0:
            print(number, "equals", divisor, "*", number // divisor)
            break
    else:
        print(number, "is a prime number")


# =========================
# BACKEND-STYLE CONDITIONS
# =========================

user_role = "admin"
is_active = True

if user_role == "admin" and is_active:
    print("Access granted")
else:
    print("Access denied")

"""
Output:
Access granted
"""


user_age = 17

if user_age < 18:
    print("User is underage")
else:
    print("User is eligible")

"""
Output:
User is underage
"""


feature_enabled = False

if not feature_enabled:
    print("Feature disabled")

"""
Output:
Feature disabled
"""
