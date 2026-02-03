"""
Basic file read/write operations.

Demonstration:
- Opening a file using context manager (with statement)
- Writing text to a file
- Automatic file closing after operation
"""

with open("content.txt", "w") as file:
    file.write("Hello from backend Python")


"""
Output:
(No console output)

File created: content.txt
File content:
Hello from backend Python
"""
