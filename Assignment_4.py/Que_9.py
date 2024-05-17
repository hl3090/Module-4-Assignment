"""
Q. Write a Python program to count the number of lines in a text file.
"""
def count_lines(file):
    with open(file,'r',encoding='utf-8') as f:
        text = f.readlines()
    return len(text)

file_name = input("Enter file name: ") 
print(count_lines(file_name))   