"""
Q. Write a Python program to read a file line by line and store it into a list.

"""

def store_in_list(file):
   try:
    with open(file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]
   except:
       return FileNotFoundError 

print(store_in_list('test.txt'))   