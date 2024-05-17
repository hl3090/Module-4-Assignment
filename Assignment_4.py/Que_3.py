"""
Q. Write a Python program to append text to a file and display the text.
"""

f = open("myfile.txt","a")
f.write("\nPython is Object Oriented Programming language")
f.write("\nHello World!")
f.close()