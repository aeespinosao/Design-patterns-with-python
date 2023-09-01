from copy import copy
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def draw(self):
        pass
    

class Square(Shape):
    
    def __init__(self, size) -> None:
        self.size = size
        
    def draw(self):
        print(f"Drawing a square of size {self.size}")
        
class Circle(Shape):
    
    def __init__(self, radius) -> None:
        self.radius = radius
        
    def draw(self):
        print(f"Drawing a circle of radius {self.radius}")
        

class AbstractArt:
    
    def __init__(self, bg_color, shapes) -> None:
        self.bg_color = bg_color
        self.shapes = shapes
        
    def draw(self):
        print(f"Background color is {self.bg_color}")
        [shape.draw() for shape in self.shapes]
        

if __name__ == "__main__":
    shapes = [Square(4), Square(5), Circle(10)]
    art1 = AbstractArt("red", shapes)
    
    
    art2 = copy(art1)
    art1.draw()
    art2.draw()
    