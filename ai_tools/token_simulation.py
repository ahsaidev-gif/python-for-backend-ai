"""
Simulating how tokens work in a prompt.
"""

prompt = input("Enter a prompt: ")

tokens = prompt.split()

# Prompt Details
print("\nSimulated Tokens:")
for token in tokens:
    print(token)

# token count
print("\n Token count:", len(tokens))

# This is not real tokenization, but it helps you understand the concept.
