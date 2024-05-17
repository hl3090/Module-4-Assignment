"""
Q. Write a Python program to copy the contents of a file to another file
"""

import shutil

# copy the contents of the demo.py file to a new file called demo1.py
shutil.copyfile('./myfile.txt', './list.txt')