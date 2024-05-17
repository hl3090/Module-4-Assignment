"""
Q. Write a Python program to count the frequency of words in a file
"""

import string

def count_word_frequency(file_name, ignore_case=True, remove_punctuation=True):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return {}
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_name}'.")
        return {}

    if not text:
        print(f"Error: File '{file_name}' is empty.")
        return {}

    if ignore_case:
        text = text.lower()

    if remove_punctuation:
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)

    words = text.split()
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

file_name = input("Enter file name: ")

word_freq = count_word_frequency(file_name, ignore_case=True, remove_punctuation=True)
print(f"The word frequency in this file is: {word_freq}.")