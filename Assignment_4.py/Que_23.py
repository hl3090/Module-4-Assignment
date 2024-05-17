"""
Q.Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
"""

# Area of Circle
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
      
    def area(self):
        area_of_circle = math.pi * self.radius * self.radius
        print(f"Area of Circle is: {area_of_circle}")
    
    def perimeter(self):    
        perimeter_of_circle = 2 * math.pi * self.radius
        print(f"Perimeter of Circle is: {perimeter_of_circle}")
        
r = int(input("Enter the value of radius: "))
area = Circle(radius=r)
print()       
area.area() 
print("-----------")
area.perimeter()           