"""
String operations commonly used in backend programs.

Demonstration:
- String slicing
- Common string methods
- Removing whitespace
- Formatted strings (f-strings)
"""

course = "Python Programming"

print(course[0:3])
print(course.upper())
print(course.strip())


first_name = "Akash"
last_name = "H S"
full_name = f"{first_name} {last_name}"
print(full_name)


"""
Output:
Pyt
PYTHON PROGRAMMING
Python Programming
Akash H S
"""
