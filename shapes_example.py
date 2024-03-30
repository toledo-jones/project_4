from geometric_shapes import *

# rectangle: A Rectangle object with length set to 10 and width to 20.
rectangle = Rectangle(10, 20)

# ellipse: An Ellipse object with semi_major_axis set to 9 and semi_minor_axis to 7.
ellipse = Ellipse(9, 7)

# square: A Square object with side set to 4.
square = Square(4)

# circle: A Circle object with radius set to 20.
circle = Circle(20)

# complex_shape: A ComplexShape object with base set to circle and holes set to [rectangle, ellipse, square].
complex_shape = ComplexShape(circle, [rectangle, ellipse, square])


# complex_shape_area: The area of complex_shape.
complex_shape_area = complex_shape.get_area()

# complex_shape_edge_length: The edge length of complex_shape.
complex_shape_edge_length = complex_shape.get_edge_length()

