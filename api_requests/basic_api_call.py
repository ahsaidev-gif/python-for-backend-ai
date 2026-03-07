"""
Basic API request example using Python.
"""

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

data = response.json()

print("Title:", data["title"])
print("Body:", data["body"])

#This example calls a public test API.