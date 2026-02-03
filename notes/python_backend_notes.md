# Python Backend Fundamentals — Learning Notes

These notes document my learning from a full Python beginner course,
rewritten and structured from a **backend and AI engineering perspective**.

**Date started:** 01-02-2026

---

## Why Python?

Python enables solving complex problems with fewer lines of code.

**Example:**

* C#: `str.Substring(0, 3)`
* JavaScript: `str.substr(0, 3)`
* Python: `str[0:3]`

Python is widely used in:

* Web applications
* Automation and testing
* Data analysis
* AI / Machine Learning
* Backend services

### What makes Python special

* High-level language (no manual memory management)
* Huge community (20+ years)
* Cross-platform (Windows, macOS, Linux)
* Large ecosystem of libraries and frameworks

---

## Python Versions

* **Python 2** → Legacy (ended in 2020)
* **Python 3** → Current and future version

---

## How Python Code Executes (High Level)

* Python source code
* Compiled to Python bytecode
* Executed by the Python Virtual Machine (PVM)
* Runs on different operating systems

This abstraction makes Python portable and developer-friendly.

---

## Expressions & Syntax

* An **expression** is code that produces a value.

```python
"*" * 3
```

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

```python
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
```

Python is case-sensitive and follows **PEP 8** style conventions.

---

## Strings

* Strings are **immutable**
* Support indexing and slicing

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

Nested loops are useful for matrix-style data.

---

## Functions

Functions help reuse logic.

```python
def greet(name):
    return f"Hi {name}"
```

Types of functions:

* Perform tasks
* Return values

### Function Arguments

* Positional
* Keyword
* Default
* Variable (`*args`)

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
* Fundamentals scale directly to real-world systems

---

## Learning Log — 02-02-2025

### Topic: **Python Lists & Dictionaries**

### Python Lists

* Ordered, mutable sequences (`[]`)
* Support indexing, negative indexing, slicing
* Assignment copies references, not values
* Slicing (`[:]`) creates a shallow copy
* Can be nested

Common operations:

* `append`, `insert`, `remove`, `pop`, `clear`
* `count`, `index`, `sort`, `reverse`, `copy`

Usage patterns:

* Stack (LIFO)
* Queue (FIFO using `collections.deque`)

Advanced concepts:

* List comprehensions
* Nested list comprehensions
* `zip()` for readable iteration
* `del` for removing items or slices

Alternative structures:

* `array`, `deque`, `heapq`, `bisect`

### Dictionaries

* Store `key : value` pairs
* Keys must be immutable
* Maintain insertion order
* Missing keys raise `KeyError`
* `dict.get()` prevents runtime errors

Creation & usage:

* `{ }`, `dict()`, comprehensions
* `items()`, `enumerate()`, `zip()`
* `sorted()`, `reversed()`, `set()`

### Key Takeaways

* Lists are powerful but require careful reference handling
* Prefer comprehensions and built-ins
* Use `deque` for queues
* Dictionaries enable fast lookups and mappings

---

## Learning Log — 03-02-2025

### Topic: **Control Flow, Loops & Functions**

### Conditional Statements

* `if / elif / else` for decision making
* `elif` avoids deep nesting
* Replaces `switch/case`

### Loops

* `for` loops iterate over sequences, not counters
* Avoid mutating collections during iteration
* Prefer copying or building new collections

### `range()`

* Lazy, memory-efficient iterable
* End value is exclusive
* Supports start, stop, step

### Loop Control

* `break` exits loops
* `continue` skips iteration
* Loop `else` runs only if no `break`
* `pass` used as placeholder

### `match` Statement (Python 3.10+)

* Structural pattern matching
* Supports literals, tuples, classes, guards
* `_` acts as wildcard
* Useful for routing and protocol handling

### Functions

* Encapsulate reusable logic
* Each call has its own local scope
* Support docstrings and annotations

### Function Arguments

* Positional, keyword, default
* `*args`, `**kwargs`
* Default mutable arguments evaluated once (pitfall)

### Special Parameters

* `/` positional-only
* `*` keyword-only
* Protect APIs and prevent breaking changes

### Lambda Expressions

* Anonymous, single-expression functions
* Used for sorting, callbacks, inline logic

### Coding Style (PEP 8)

* 4-space indentation
* 79-character line length
* Meaningful names
* Readability over cleverness

### Looping Techniques

* `enumerate()`, `items()`, `zip()`
* `sorted()` for ordered iteration
* `set()` for uniqueness
* Prefer new collections over mutation

### Conditions & Comparisons

* Chained comparisons
* Membership (`in`, `not in`)
* Identity (`is`, `is not`)
* Boolean operators are short-circuiting

### Compound Statements

* Multi-line blocks (`if`, `for`, `while`, `try`, `with`, `match`)
* Indentation defines scope

### Key Takeaways

* Control flow defines program behavior
* Readability matters as much as correctness
* `match` enables expressive logic
* Clean functions = maintainable APIs

