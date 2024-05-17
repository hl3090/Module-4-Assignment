"""
Q. Write a Python program to read last n lines of a file.
"""
def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as f:
        lines = f.readlines()[-n:]
        for line in lines:
            print(line.strip())

read_last_n_lines('myfile.txt', 1)

