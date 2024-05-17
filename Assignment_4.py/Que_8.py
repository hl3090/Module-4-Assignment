"""
Q. Write a python program to find the longest words.
"""

def find_long_word(file):
    with open(file,'r',encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    max_length = max(len(word) for word in words)
    longest_word = []

    for word in words:
        if len(word) == max_length:
           longest_word.append(word)
    
    return longest_word       
        
file_name = input("Enter file name: ")
long_word = find_long_word(file_name)
print(f"The longest word in the file is: {long_word}.")
