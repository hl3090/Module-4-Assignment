"""
Q. When will the else part of try-except-else be executed?
Ans. The else block in a try-except statement is executed if no exception is raised in the try block.

"""
# Example
class oddexception(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num % 2==0:
        print("It is an even number")
    else:
        raise oddexception
    
except oddexception:
    print("It is not an even number")
except:
    print("Invalid input")            
