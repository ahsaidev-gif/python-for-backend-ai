"""
Reactivation exercise after break.
Simulating simple backend data processing.
"""

import pandas as pd

data = {
    "id": [1, 2, 3, 4],
    "name": ["Akash", "Ravi", "Meera", None],
    "role": ["Engineer", "Engineer", "Manager", "Engineer"],
    "active": [True, False, True, True]
}

df = pd.DataFrame(data)

# Clean missing names
df["name"] = df["name"].fillna("UNKNOWN")

# Filter active users
active_users = df[df["active"] == True]

# Group by role
summary = active_users.groupby("role").count()

print(summary)