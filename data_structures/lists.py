"""
List examples commonly used in backend-style programs.

Demonstration:
- Creating and modifying lists
- Iteration and enumeration
- Slicing, unpacking, and searching
- Sorting simple and complex data
"""

documents = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
documents.append("doc4.pdf")

for document in documents:
    print(document)


"""
Output:
doc1.pdf
doc2.pdf
doc3.pdf
doc4.pdf
"""


letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)


"""
Output:
0 a
1 b
2 c
"""


numbers = list(range(20))
characters = list("Hello World")

print(len(characters))


"""
Output:
11
"""


letters = ["a", "b", "c", "d"]
letters[0] = "A"

print(letters[0:3])
print(letters[::2])


"""
Output:
['A', 'b', 'c']
['A', 'c']
"""


numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *others, last = numbers

print(first, last)
print(others)


"""
Output:
1 9
[2, 3, 4, 4, 4, 4]
"""


letters = ["a", "b", "c"]

letters.append("d")
letters.insert(0, "-")

letters.pop(0)
letters.remove("b")
letters.clear()

print(letters)


"""
Output:
[]
"""


letters = ["a", "b", "c"]

print(letters.count("d"))

if "d" in letters:
    print(letters.index("d"))


"""
Output:
0
"""


numbers = [3, 51, 2, 8, 6]

print(sorted(numbers, reverse=True))
print(numbers)


"""
Output:
[51, 8, 6, 3, 2]
[3, 51, 2, 8, 6]
"""


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
print(items)


"""
Output:
[('Product2', 9), ('Product1', 10), ('Product3', 12)]
"""
