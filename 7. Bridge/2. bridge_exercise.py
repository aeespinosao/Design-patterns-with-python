"""
Bridge Coding Exercise
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.
Please refactor this hierarchy, giving the base class Shape  a constructor that takes an interface Renderer  defined as
class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
as well as VectorRenderer  and RasterRenderer  classes. Each inheritor of the Shape  abstract class should have a constructor that takes a Renderer  such that, subsequently, each constructed object's __str__()  operates correctly, for example,
str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels" 
"""

from abc import ABC

class Shape:
    def __init__(self, renderer, name):
        self.name = name
        self.renderer = renderer
    
    def __str__(self):
        return "Drawing {} as {}".format(self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
    
class VectorRenderer(Renderer):
    def what_to_render_as(self):
        return 'lines'
        
class RasterRenderer(Renderer):
    def what_to_render_as(self):
        return 'pixels'
        
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

import unittest  
class Evaluate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), 'Drawing Triangle as pixels')