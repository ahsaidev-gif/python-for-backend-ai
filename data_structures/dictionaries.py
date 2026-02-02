"""
Dictionary examples representing metadata.
"""

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
Basic dictionary access using get().
Prevents runtime errors in APIs.
"""

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer.get("name"))


"""
Dictionary mapping example.
Used in normalization and transformation layers.
"""

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
Emoji/text replacement using dictionary lookup.
Used in chat processing and NLP pipelines.
"""

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
