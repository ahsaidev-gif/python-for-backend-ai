"""
Basic JSON handling for backend systems. 
"""

import json

#Python dictionary
user = {
    "id": 1,
    "name": "Akash",
    "role": "Engineer",
    "skills": ["Python", "Backend", "AI"],
    "active": True
}

#Save dictionary to JSON file
with open("user_data.json", "w") as file:
    json.dump(user, file, indent=4)

print("JSON file created")

#Read JSON file
with open("user_data.json", "r") as file:
    data = json.load(file)

print("Loaded Data:")
print(data)

print("User Name:", data["name"])

