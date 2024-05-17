"""
Q.How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
"""

# Example
try:
    num1 = int(input("Enter a number 1: "))
    num2 = int(input("Enter a number 2 : "))
    
    print(num1/num2)
    
except ZeroDivisionError:
    print("Number cannot divide by zero ")
except ValueError:
    print("Invalid input")     
finally:
    print("Hope you performed all the operations!!") 