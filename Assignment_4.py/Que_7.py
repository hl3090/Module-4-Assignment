"""
Q. Write a Python program to read a file line by line store it into a variable.

"""

file_name = input("Enter file name: ")
lines = []

try:
    with open(file_name, 'r', encoding='utf-8') as f:
      for line in f:
        lines.append(line.strip())
except FileNotFoundError:
   print(f"Error: {file_name} not found")

print_lines = '\n'.join(lines)
print(print_lines)
