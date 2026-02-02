"""
List examples used in backend-style programs.
"""

documents = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]

documents.append("doc4.pdf")

for doc in documents:
    print(doc)

"""
Enumerate over a list with index and value.
Common in logging, batch processing, and pipelines.
"""

letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)


"""
Create lists from ranges and strings.
Used for indexing, tokenization, and preprocessing.
"""

numbers = list(range(20))
chars = list("Hello World")

print(len(chars))

"""
List slicing and step operations.
Useful for pagination, sampling, and chunking.
"""

letters = ["a", "b", "c", "d"]
letters[0] = "A"

print(letters[0:3])
print(letters[::2])


"""
Unpacking lists into head, body, and tail.
Helpful for request parsing and stream handling.
"""

numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *others, last = numbers

print(first, last)
print(others)


"""
Adding and removing items from lists.
Used in task queues and mutable collections.
"""

letters = ["a", "b", "c"]

letters.append("d")
letters.insert(0, "-")

letters.pop(0)
letters.remove("b")
letters.clear()

print(letters)

"""
Counting and searching list elements.
Used in validations and analytics.
"""

letters = ["a", "b", "c"]

print(letters.count("d"))

if "d" in letters:
    print(letters.index("d"))

"""
Sorting lists without mutating original data.
Important for predictable backend behavior.
"""

numbers = [3, 51, 2, 8, 6]

print(sorted(numbers, reverse=True))
print(numbers)


"""
Sorting complex data using a key function.
Common in business rules and reports.
"""

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
print(items)
