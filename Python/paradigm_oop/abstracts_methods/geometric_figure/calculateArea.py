"""
This module defines an abstract class for geometric
figures and implements specific geometric figures
 
File: calculateArea.py
Author: Anthony Bañon
Created: 2025-06-05
Last Updated: 2025-06-05
"""


from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def calculateArea(self):
        """Calculate the area of the geometric figure."""
        pass

class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14 * self.radius * self.radius

class Rectangle(GeometricFigure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        return self.base * self.height

class Triangle(GeometricFigure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        return 0.5 * self.base * self.height
    
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4)
    print(f"Circle area: {circle.calculateArea()}")
    print(f"Rectangle area: {rectangle.calculateArea()}")
    print(f"Triangle area: {triangle.calculateArea()}")
