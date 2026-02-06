"""
Basic file read/write operations.

Demonstration:
- Opening a file using context manager (with statement)
- Writing text to a file
- Automatic file closing after operation
"""

import glob
import json
with open("content.txt", "w") as file:
    file.write("Hello from backend Python")


"""
Output:
(No console output)

File created: content.txt
File content:
Hello from backend Python
"""

"""
File handling, compilation behavior, JSON serialization,
and filesystem utilities.
"""

# =========================
# FILE WRITE (TEXT MODE)
# =========================

with open("example.txt", "w", encoding="utf-8") as f:
    f.write("This is a test file.\n")
    f.write("Python file handling example.")

print("File written successfully.")

"""
Output:
File written successfully.
"""


# =========================
# FILE READ
# =========================

with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)

"""
Output:
This is a test file.
Python file handling example.
"""


# =========================
# READ LINE BY LINE
# =========================

with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

"""
Output:
This is a test file.
Python file handling example.
"""


# =========================
# FILE POSITIONING
# =========================

with open("example.txt", "r", encoding="utf-8") as f:
    print(f.tell())
    f.seek(5)
    print(f.read(4))

"""
Output:
0
is a
"""


# =========================
# BINARY FILE COPY (IMAGE / FILE)
# =========================

with open("source.bin", "wb") as f:
    f.write(b"0123456789abcdef")

with open("source.bin", "rb") as src, open("copy.bin", "wb") as dst:
    for chunk in src:
        dst.write(chunk)

print("Binary file copied.")

"""
Output:
Binary file copied.
"""


# =========================
# JSON SERIALIZATION
# =========================


data = {
    "service": "backend",
    "version": 1,
    "enabled": True
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

print("JSON saved.")

"""
Output:
JSON saved.
"""


# =========================
# JSON DESERIALIZATION
# =========================

with open("config.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data)

"""
Output:
{'service': 'backend', 'version': 1, 'enabled': True}
"""


# =========================
# FILE WILDCARDS
# =========================


python_files = glob.glob("*.py")
print(python_files)

"""
Output:
['filehandling.py']
"""
