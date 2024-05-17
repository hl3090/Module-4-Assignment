"""
Q.Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
"""
# find area of Rectangle

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def display(self):
        ans = self.length * self.breadth
        print(f"Area of rectangle is : {ans}")
        
        
l = int(input("Enter value of length: ")) 
b = int(input("Enter value of breadth: "))       
area = Rectangle(length=l,breadth=b)
print("-----------")
area.display()        
            
