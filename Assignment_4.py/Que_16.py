"""
Q. Can one block of except statements handle multiple exception?
Ans. It is possible for a single except block to handle multiple exceptions. You can specify multiple exception classes, separated 
     by commas, in the except statement.
"""

#Example
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    ans = a/b 
    print(ans)
    
except (ZeroDivisionError, ValueError):    # this except block is handling multiple exceptions
    print("An error occurred!")