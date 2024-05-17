"""
Q. Write a Python program to write a list to a file.
"""

def list_to_file(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")

file_name = input("Enter file name: ")
data = ['python', 'java', 'php']

list_to_file(file_name, data)
print(f"Data added successfully in {file_name}.")

