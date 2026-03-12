"""
Example of sending a POST request with JSON Payload.
"""

import requests

url = "htttps://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "AI Prompt Example",
    "body": "Explain what artifical intelligence is",
    "userId": 1
}

response = requests.post(url, json=payload)

data = response.json()

print("Response from  API")
print(data)

