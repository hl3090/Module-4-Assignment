"""
Q. How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
Ans. 1) class : class is a collection of data member and member functions
          class is a datatype

    2) object : object is an instance or variable of class

    note: class always declare with class keyword.

    syntax:

    class <classname>:
        body of class
  
        
Self -: In Python, self is a reference to the current instance of a class. It is used as the first parameter in instance methods, and 
       it allows you to access and manipulate the attributes and behaviors of the instance.      

"""

# Example of Class in Python
class Square:
    def __init__(self,side):
        self.side = side * side
        
    def display(self):
        ans = self.side 
        print(f"Area of Square is : {ans}")
        
        
s = int(input("Enter value of side: "))       
area = Square(side=s)
print("-----------")
area.display()        
            
