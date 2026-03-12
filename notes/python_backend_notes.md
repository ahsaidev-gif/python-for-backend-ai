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

## Learning Log — Day 8 — 08-02-2026


```python
"""
Pandas Fundamentals — 10 Minutes Overview

This file contains hands-on examples covering:
- Core pandas data structures (Series, DataFrame)
- Data creation and inspection
- Indexing and selection
- Sorting, filtering, and boolean indexing
- Missing data handling
- Aggregations and transformations
- Merging, grouping, reshaping
- Time series operations
- Categorical data
- Plotting basics
- Importing and exporting data

The examples follow pandas documentation style and are used
to understand data processing workflows commonly required
in backend and AI systems.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

## Basic Data Structures

### Series

```python
series_example = pd.Series([1, 3, 5, np.nan, 6, 8])
series_example
```

---

### DataFrame with Date Index

```python
dates = pd.date_range("20130101", periods=6)

data_frame = pd.DataFrame(
    np.random.randn(6, 4),
    index=dates,
    columns=list("ABCD")
)

data_frame
```

---

### DataFrame from Dictionary

```python
data_frame_mixed = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

data_frame_mixed
```

```python
data_frame_mixed.dtypes
```

---

## Viewing Data

```python
data_frame.head()
data_frame.tail(3)
data_frame.index
data_frame.columns
```

```python
data_frame.to_numpy()
data_frame_mixed.to_numpy()
```

```python
data_frame.describe()
data_frame.T
```

---

## Sorting

```python
data_frame.sort_index(axis=1, ascending=False)
data_frame.sort_values(by="B")
```

---

## Selection

### Column Selection

```python
data_frame["A"]
data_frame.A
data_frame[["B", "A"]]
```

### Row Selection

```python
data_frame[0:3]
data_frame["20130102":"20130104"]
```

### Label-Based Selection

```python
data_frame.loc[dates[0]]
data_frame.loc[:, ["A", "B"]]
data_frame.loc["20130102":"20130104", ["A", "B"]]
data_frame.at[dates[0], "A"]
```

### Position-Based Selection

```python
data_frame.iloc[3]
data_frame.iloc[3:5, 0:2]
data_frame.iloc[[1, 2, 4], [0, 2]]
data_frame.iat[1, 1]
```

---

## Boolean Indexing

```python
data_frame[data_frame["A"] > 0]
data_frame[data_frame > 0]
```

```python
data_frame_filter = data_frame.copy()
data_frame_filter["E"] = ["one", "one", "two", "three", "four", "three"]

data_frame_filter[data_frame_filter["E"].isin(["two", "four"])]
```

---

## Setting Data

```python
series_alignment = pd.Series(
    [1, 2, 3, 4, 5, 6],
    index=pd.date_range("20130102", periods=6)
)

data_frame["F"] = series_alignment
data_frame.at[dates[0], "A"] = 0
data_frame.iat[0, 1] = 0
data_frame.loc[:, "D"] = np.array([5] * len(data_frame))
```

---

## Missing Data

```python
data_frame_reindexed = data_frame.reindex(
    index=dates[0:4],
    columns=list(data_frame.columns) + ["E"]
)

data_frame_reindexed.dropna(how="any")
data_frame_reindexed.fillna(value=5)
pd.isna(data_frame_reindexed)
```

---

## Operations & Statistics

```python
data_frame.mean()
data_frame.mean(axis=1)
```

```python
shifted_series = pd.Series(
    [1, 3, 5, np.nan, 6, 8],
    index=dates
).shift(2)

data_frame.sub(shifted_series, axis="index")
```

---

## Aggregation & Transformation

```python
data_frame.agg(lambda col: np.mean(col) * 5.6)
data_frame.transform(lambda col: col * 101.2)
```

---

## Value Counts

```python
random_series = pd.Series(np.random.randint(0, 7, size=10))
random_series.value_counts()
```

---

## String Methods

```python
string_series = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"]
)

string_series.str.lower()
```

---

## Concatenation

```python
concat_frame = pd.DataFrame(np.random.randn(10, 4))
frames = [concat_frame[:3], concat_frame[3:7], concat_frame[7:]]
pd.concat(frames)
```

---

## Merge / Join

```python
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

pd.merge(left, right, on="key")
```

---

## Grouping

```python
group_frame = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

group_frame.groupby("A")[["C", "D"]].sum()
group_frame.groupby(["A", "B"]).sum()
```

---

## Reshaping

```python
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]

multi_index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
reshape_frame = pd.DataFrame(np.random.randn(8, 2), index=multi_index, columns=["A", "B"])

stacked = reshape_frame[:4].stack()
stacked.unstack()
```

---

## Pivot Tables

```python
pivot_frame = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

pd.pivot_table(pivot_frame, values="D", index=["A", "B"], columns=["C"])
```

---

## Time Series

```python
time_index = pd.date_range("1/1/2012", periods=100, freq="s")
time_series = pd.Series(np.random.randint(0, 500, len(time_index)), index=time_index)

time_series.resample("5Min").sum()
```

---

## Categoricals

```python
category_frame = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

category_frame["grade"] = category_frame["raw_grade"].astype("category")
category_frame["grade"] = category_frame["grade"].cat.rename_categories(
    ["very good", "good", "very bad"]
)
```

---

## Plotting

```python
plot_series = pd.Series(np.random.randn(1000)).cumsum()
plot_series.plot()
plt.close("all")
```

---

## Import / Export

```python
export_frame = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
export_frame.to_csv("example.csv")
pd.read_csv("example.csv")
```

---

## Key Takeaways

* Pandas is built for labeled, structured data
* Index alignment is automatic and powerful
* Selection APIs (`loc`, `iloc`) are essential for correctness
* Grouping, reshaping, and merging are core backend workflows
* Pandas forms the foundation for AI data pipelines

## Learning Log — Day 9 — 09-02-2026

# Select specific column
names = df["name"]
print(names)

# Filter active users
active_users = df[df["active"] == True]
print(active_users)

# Handle missing values
df_filled = df.fillna("UNKNOWN")
print(df_filled)


## Pandas Filtering & Cleaning (Backend Perspective)

Pandas is commonly used to:
- Select required columns
- Filter records based on conditions
- Handle missing or incomplete data

These steps are critical before passing data
to downstream AI or backend services.

## Learning Log — Day 10 — 06-03-2026

## JSON Handling (Backend Perspective)

JSON is the most common data exchange format used in APIs and AI systems.

Python uses the built-in json module to:
- Convert dictionaries to JSON files
- Load JSON files into Python dictionaries

Common functions:
json.dump()  → write JSON
json.load()  → read JSON

## Learning Log — Day 11 — 07-03-2026

## APIs and HTTP Requests (Backend Perspective)

APIs allow programs to communicate with external services.

Common request types:
GET  → retrieve data
POST → send data

Python uses the requests library to call APIs.

API responses are usually returned in JSON format.

## Learning Log — Day 12 — 11-03-2026

## Prompt Payloads (AI Systems)

AI APIs receive requests in the form of JSON payloads.

A payload usually includes:
- prompt → user instruction
- temperature → randomness control
- max_tokens → response length

Python converts dictionaries into JSON payloads before sending them to the AI API.

## Learning Log — Day 12 — 11-03-2026

## AI Prompt Flow

Basic AI systems follow this flow:

User Prompt → Processing → Response

In real applications:
Python backend sends the prompt to an AI API and receives the generated response.

## Learning Log — Day 13 — 12-03-2026

## POST Requests (API Communication)

POST requests are used to send data to an API.

In AI systems:
Python sends prompts as JSON payloads using POST requests.

The API processes the request and returns a JSON response.

