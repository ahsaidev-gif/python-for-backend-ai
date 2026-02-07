# Python Backend Fundamentals — Learning Notes

These notes track what I learned while studying Python basics, written in simple terms and focused on **backend and AI use cases**.

---

## Learning Log — Day 1 — 01-02-2026

### Topic: Python Basics

---

## Why Python?

Python helps solve problems with fewer lines of code.

Example:

* C#: `str.Substring(0, 3)`
* JavaScript: `str.substr(0, 3)`
* Python: `str[0:3]`

Python is commonly used for:

* Web applications
* Automation and testing
* Data analysis
* AI / Machine Learning
* Backend services

### What Makes Python Special

* Easy to read and write
* Large community and libraries
* Works on Windows, macOS, and Linux
* No manual memory management

---

## Python Versions

* Python 2 — legacy version (ended in 2020)
* Python 3 — current and future version

---

## How Python Code Runs

* Python code is written in `.py` files
* Converted into bytecode
* Executed by the Python Virtual Machine (PVM)
* Same code runs on different operating systems

---

## Expressions & Syntax

An expression is code that produces a value.

```python
"*" * 3
```

* Syntax errors happen when grammar is wrong
* Linters help catch issues early

---

## Variables & Data Types

Variables store data and act as labels.

Basic data types:

* `int`
* `float`
* `bool`
* `str`

```python
students_count = 1000
course_rating = 4.99
is_published = False
course_name = "Python Programming"
```

Python is case-sensitive and follows PEP 8 style rules.

---

## Strings

* Strings are immutable
* Support indexing and slicing

```python
course_name = "Python Programming"
course_name[0:3]
course_name[-1]
```

Common methods:

* `upper()`, `lower()`
* `strip()`
* `find()`, `replace()`

Formatted strings:

```python
full_name = f"{first_name} {last_name}"
```

---

## Numbers & Math

Python supports integers, floats, and complex numbers.

Operators:

```python
+  -  *  /  //  %  **
```

Math module example:

```python
import math
math.ceil(2.2)
```

---

## Type Conversion

User input is always a string.

```python
number = int(input("Enter number: "))
result = number + 1
```

Common conversions:

* `int()`
* `float()`
* `bool()`
* `str()`

---

## Truthy & Falsy Values

Falsy values:

* `0`
* `""`
* `None`

Everything else is truthy.

```python
bool("False")
```

---

## File Handling (Basic)

```python
with open("content.txt", "w") as file:
    file.write("Hello")
```

Using `with` ensures the file closes properly.

---

## Key Takeaways

* Python is simple but powerful
* Clear syntax improves productivity
* Core basics apply directly to backend systems

---

## Learning Log — Day 2 — 02-02-2026

### Topic: Lists & Dictionaries

---

## Lists

* Ordered and mutable
* Written using `[]`
* Support indexing and slicing
* Can contain nested lists

Common operations:

* `append`, `insert`
* `remove`, `pop`
* `count`, `index`
* `sort`, `reverse`

Usage patterns:

* Stack (LIFO)
* Queue (FIFO using `deque`)

Advanced topics:

* List comprehensions
* `zip()` for looping
* `del` for removing items or slices

Other data structures:

* `array`
* `deque`
* `heapq`
* `bisect`

---

## Dictionaries

* Store key-value pairs
* Keys must be immutable
* Maintain insertion order
* Missing keys raise errors
* `get()` safely handles missing keys

Creation and looping:

* `{}`, `dict()`
* `items()`
* `enumerate()`
* `zip()`

---

## Key Takeaways

* Lists are flexible but mutable
* Dictionaries enable fast lookups
* Built-in tools improve readability

---

## Learning Log — Day 3 — 03-02-2026

### Topic: Control Flow, Loops & Functions

---

## Conditional Statements

Used to make decisions.

```python
if temperature > 30:
    print("Warm")
elif temperature > 20:
    print("Nice")
else:
    print("Cold")
```

* `elif` avoids deep nesting
* Indentation defines blocks

---

## Loops

### For Loop

Used to loop over sequences.

```python
for char in "Python":
    print(char)
```

### While Loop

Used when looping depends on a condition.

```python
while user_command.lower() != "quit":
    user_command = input(">")
```

---

## range()

* Generates numbers
* End value is not included
* Memory efficient

```python
range(5)
range(1, 10)
range(1, 10, 2)
```

---

## Loop Control

* `break` stops the loop
* `continue` skips iteration
* `pass` is a placeholder

### Loop else

Runs only if the loop finishes without `break`.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, "is prime")
```

---

## Functions

Functions group reusable logic.

```python
def greet_user(name):
    return f"Hi {name}"
```

Argument types:

* Positional
* Keyword
* Default
* `*args`, `**kwargs`

---

## Key Takeaways

* Control flow defines program behavior
* Functions improve reuse and clarity
* Clean logic matters in backend code

---

## Learning Log — Day 4 — 04-02-2026

### Topic: Conditionals & Logical Operators

---

## Logical Operators

* `and` → all conditions true
* `or` → any condition true
* `not` → reverses condition

```python
if has_income or has_good_credit:
    print("Eligible")
```

---

## Comparison Operators

* `==`, `!=`
* `>`, `<`, `>=`, `<=`
* `in`, `not in`
* `is`, `is not`

Chained comparison:

```python
a < b == c
```

---

## Backend Use

Conditionals are used for:

* Validation
* Access checks
* Feature flags
* Business rules

---

## Key Takeaways

* Indentation controls logic
* Logical operators short-circuit
* Clear conditions improve maintainability

---

## Learning Log — Day 5 — 05-02-2026

### Topic: range() and Functions

---

## range() in Practice

* Does not store values
* Efficient for loops
* Works with `sum()` and `len()`

---

## Iterating with Index

```python
for index, value in enumerate(items):
    print(index, value)
```

---

## Functions

* Defined using `def`
* Indentation is required
* Can include docstrings

Return values:

* Functions return `None` by default
* Returning values is preferred in backend code

---

## Default Arguments

* Evaluated once
* Mutable defaults can cause bugs
* Use `None` instead

---

## Lambda Functions

* Short, one-line functions
* Commonly used for sorting

```python
items.sort(key=lambda item: item[1])
```

---

## Key Takeaways

* `range()` is memory efficient
* Functions structure backend logic
* Argument handling affects API design

---

## Learning Log — Day 6 — 06-02-2026

### Topic: File Handling, Compiled Files & JSON

---

## Compiled Python Files (`.pyc`)

* Python converts `.py` files into bytecode
* Stored in the `__pycache__` folder
* Filename includes Python version

Example:

```
__pycache__/spam.cpython-311.pyc
```

Key points:

* Compilation is automatic
* Recompiled only if source changes
* Platform-independent
* Improves load time, not execution speed

---

## Reading and Writing Files

```python
open(filename, mode, encoding)
```

Common modes:

* `r` → read
* `w` → write
* `a` → append
* `r+` → read and write
* `b` → binary

---

## Text vs Binary Mode

* Text mode works with strings
* Binary mode works with bytes
* Required for images and executables

---

## Using `with`

```python
with open("workfile.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

* File closes automatically
* Safer than manual `close()`

---

## Working with JSON

```python
import json
```

Writing:

```python
json.dump(data, file)
```

Reading:

```python
data = json.load(file)
```

* JSON uses UTF-8
* Used in APIs and configuration

---

## File Wildcards

```python
import glob
glob.glob("*.py")
```

---

## Key Takeaways

* Always use `with` for files
* Use binary mode for non-text files
* JSON is standard for backend data
* File handling is a core backend skill

## Learning Log — Day 7 — 07-02-2026

## Week 1 Reflection

In the first week, I covered Python fundamentals required for backend
and AI system development.

I can now:
- Use lists and dictionaries for structured data
- Apply control flow for decision making
- Write reusable functions
- Handle basic file input/output

These concepts will be reused in future AI and backend projects.


