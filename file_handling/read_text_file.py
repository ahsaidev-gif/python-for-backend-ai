"""
Basic file handling examples used in backend programs.

Demonstration:
- Reading and writing text files
- Using context managers (with statement)
- File positioning
- Binary file handling
- JSON serialization and deserialization
- File discovery using wildcards
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


with open("example.txt", "w", encoding="utf-8") as file:
    file.write("This is a test file.\n")
    file.write("Python file handling example.")

print("File written successfully.")


"""
Output:
File written successfully.
"""


with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)


"""
Output:
This is a test file.
Python file handling example.
"""


with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


"""
Output:
This is a test file.
Python file handling example.
"""


with open("example.txt", "r", encoding="utf-8") as file:
    print(file.tell())
    file.seek(5)
    print(file.read(4))


"""
Output:
0
is a
"""


with open("source.bin", "wb") as file:
    file.write(b"0123456789abcdef")

with open("source.bin", "rb") as source_file, open("copy.bin", "wb") as destination_file:
    for chunk in source_file:
        destination_file.write(chunk)

print("Binary file copied.")


"""
Output:
Binary file copied.
"""


data = {
    "service": "backend",
    "version": 1,
    "enabled": True
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

print("JSON saved.")


"""
Output:
JSON saved.
"""


with open("config.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(loaded_data)


"""
Output:
{'service': 'backend', 'version': 1, 'enabled': True}
"""


python_files = glob.glob("*.py")
print(python_files)


"""
Output:
['filehandling.py']
"""
