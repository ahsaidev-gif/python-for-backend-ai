"""
Dictionary examples commonly used in backend programs.

Demonstration:
- Storing and updating metadata
- Iterating over dictionary key-value pairs
- Safe access using get()
- Dictionary-based mapping and transformation
- Text replacement using dictionary lookup
"""

# =========================
# METADATA DICTIONARY
# =========================

document = {
    "id": 1,
    "name": "policy.pdf",
    "pages": 12,
    "processed": True
}

print(document["name"])

document["pages"] = 15

for key, value in document.items():
    print(key, value)


"""
Output:
policy.pdf
id 1
name policy.pdf
pages 15
processed True
"""


# =========================
# SAFE DICTIONARY ACCESS
# =========================

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer.get("name"))


"""
Output:
John Smith
"""


# =========================
# DICTIONARY MAPPING
# =========================
# Sample input assumed: 1345

phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)


"""
Sample Output:
Phone: 1345
One Three Four !
"""


# =========================
# TEXT / EMOJI REPLACEMENT
# =========================
# Sample input assumed: Good morning :)

message = input("> ")
words = message.split(" ")

emojis = {
    ":)": "emoji",
    ":(": "sad"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)


"""
Sample Output:
> Good morning :)
Good morning emoji
"""
