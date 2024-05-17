"""
Q.How many except statements can a try-except block have? Name Some built-in exception classes:

"""
# A try-except block can have multiple except statements, each one handling a different type of exception.
# Example

try:
    a = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")    # this exception is for zerodivision error
except ValueError:
    print("Invalid value!")    # this exception is for value error
