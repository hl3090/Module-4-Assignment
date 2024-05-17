"""
Q.What is used to check whether an object o is an instance of class A?
Ans. In Python, you can use the isinstance() function to check if an object is an instance of a specific class. 

"""
# Example
class A:
    name = "Hatim"

o = A()

isinstance(o, A)  # returns True