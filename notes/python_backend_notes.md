
# Python Backend Fundamentals — Learning Notes

These notes document my learning from a full Python beginner course,
rewritten and structured from a **backend and AI engineering perspective**.

Date started: 01-02-2026

---

## Why Python?

Python enables solving complex problems with fewer lines of code.

Example:
- C#: `str.Substring(0, 3)`
- JavaScript: `str.substr(0, 3)`
- Python: `str[0:3]`

Python is widely used in:
- Web applications
- Automation and testing
- Data analysis
- AI / Machine Learning
- Backend services

### What makes Python special
- High-level language (no manual memory management)
- Huge community (20+ years)
- Cross-platform (Windows, macOS, Linux)
- Large ecosystem of libraries and frameworks

---

## Python Versions

- Python 2 → Legacy (ended in 2020)
- Python 3 → Current and future version

---

## How Python Code Executes (High Level)

- Python source code
- Compiled to Python bytecode
- Executed by Python Virtual Machine (PVM)
- Runs on different operating systems

This abstraction makes Python portable and developer-friendly.

---

## Expressions & Syntax

- An **expression** is code that produces a value.

Example:
```python
"*" * 3
````

* **Syntax errors** occur due to invalid grammar.
* **Linters** detect issues before runtime.

---

## Variables & Data Types

Variables store data in memory and act as labels.

Primitive data types:

* `int`
* `float`
* `bool`
* `str`

Example:

```python
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
```

Python is case-sensitive and follows PEP8 style conventions.

---

## Strings

Strings are immutable and support slicing.

Example:

```python
course = "Python Programming"
course[0:3]   # 'Pyt'
course[-1]    # 'g'
```

Common string methods:

* `upper()`, `lower()`, `title()`
* `strip()`, `lstrip()`, `rstrip()`
* `find()`, `replace()`

Formatted strings:

```python
full_name = f"{first} {last}"
```

---

## Numbers & Math

Python supports:

* Integers
* Floats
* Complex numbers

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

Input values are strings by default.

Example:

```python
x = int(input("Enter number: "))
y = x + 1
```

Conversions:

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

Example:

```python
bool("False")  # True
```

---

## Control Flow

### Conditional Statements

```python
if temperature > 30:
    print("Warm")
elif temperature > 20:
    print("Nice")
else:
    print("Cold")
```

### Ternary Operator

```python
message = "Eligible" if age >= 18 else "Not eligible"
```

### Logical Operators

* `and`
* `or`
* `not`

---

## Loops

### For Loop

```python
for i in range(3):
    print(i)
```

### While Loop

```python
while command.lower() != "quit":
    command = input(">")
```

### Iterables

* `range`
* `string`
* `list`

Nested loops can be used for matrix-style data.

---

## Functions

Functions help reuse logic.

Example:

```python
def greet(name):
    return f"Hi {name}"
```

Types:

* Functions that perform tasks
* Functions that return values

### Arguments

* Positional
* Keyword
* Default
* Variable (`*args`)

Example:

```python
def multiply(*numbers):
    total = 1
    for n in numbers:
        total *= n
    return total
```

---

## File Handling

Used for reading and writing data.

Example:

```python
with open("content.txt", "w") as file:
    file.write("Hello")
```

---

## Backend & AI Perspective

These Python fundamentals are essential for:

* Document ingestion
* Metadata processing
* Data preprocessing
* API-based AI services
* RAG pipelines and LLM orchestration

---

## Key Takeaways

* Python acts as glue code for backend AI systems
* Clean, readable code is more valuable than clever tricks
* These fundamentals will be reused across all future AI projects

##  Learning Log

###  02-02-2025

### Topic: **Python Lists & Dictionaries**

---

##  Concepts Learned

###  Python Lists

* Lists are **ordered, mutable sequences** written using `[]`.
* Can store **multiple data types**, though usually homogeneous.
* Support:

  * Indexing
  * Negative indexing
  * Slicing

* Unlike strings, lists are **mutable**.
* Assignment copies **references**, not values.
* Slicing (`[:]`) creates a **shallow copy**.
* Lists can be **nested**.
* Common list operations:

  * `append`, `insert`, `remove`, `pop`, `clear`
  * `count`, `index`, `sort`, `reverse`, `copy`
* Lists can act as:

  * **Stacks (LIFO)** using `append()` and `pop()`
  * **Queues (FIFO)** using `collections.deque`

* **List comprehensions** provide concise and readable list creation.
* Nested list comprehensions can replace nested loops.
* Prefer built-in functions like `zip()` for readability.
* `del` can remove:

  * Individual items
  * Slices
  * Entire lists
* Alternative data structures for performance:

  * `array` → compact numeric storage
  * `deque` → fast queue operations
  * `heapq` → priority queues
  * `bisect` → sorted list insertion

---

###  Dictionaries

* Dictionaries store **key : value** pairs.
* Keys must be **immutable**:

  * strings
  * numbers
  * tuples
* Values can be of any type.
* Accessing a missing key raises a **KeyError**.
* Use `dict.get()` to safely access keys.
* Dictionaries maintain **insertion order**.
* Common dictionary operations:

  * Add or update values
  * Delete keys using `del`
  * Check key existence using `in`
* Dictionary creation methods:

  * Literal `{ }`
  * `dict()` constructor
  * Dictionary comprehensions
* Looping techniques:

  * `items()` → key & value
  * `enumerate()` → index & value
  * `zip()` → loop multiple sequences
  * `sorted()`, `reversed()`, `set()`

---

##  Key Takeaways

* Lists are **powerful but mutable** — reference handling is important.
* Prefer **list comprehensions** and **built-ins** for clean code.
* Use `deque` instead of lists for queue implementations.
* Dictionaries are ideal for **fast lookups and mappings**.
* `dict.get()` prevents runtime errors from missing keys.


