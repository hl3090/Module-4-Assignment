"""
Q. Write python program that user to enter only odd numbers, else will raise an exception.
"""

# Example
class Evenexception(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num % 2!=0:
        print("It is an odd number")
    else:
        raise Evenexception
    
except (Evenexception,ValueError):
    print("It is not an odd number")
except:
    print("Invalid input")            
