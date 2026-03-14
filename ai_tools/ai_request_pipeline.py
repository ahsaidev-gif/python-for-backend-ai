"""
Understanding the AI request pipeline
"""

import json
import requests

prompt = input("Enter a prompt: ")

payload = {
    "prompt": prompt,
    "temperature": 0.2,
    "max_tokens": 100
}

# prompt send
print("\nPayload that would be sent to an AI API:")
print(json.dumps(json=payload, indent=4))

# AI endpoint
url = "https://jsonplaceholder.typicode/posts"

response = requests.post(url, json=payload)

print("\nSimulated API Response:")
print(response.json())
