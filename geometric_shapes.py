from math import pi, sqrt


class GeometricShape:
    def __init__(self, name: str) -> None:
        """
        Parent class for Geometric Shapes
        @param name: Label for this shape
        """
        self.set_name(name)

    def get_name(self) -> str:
        """
        Get Label for this shape
        @return: Label for this shape
        """
        return self.__name

    def set_name(self, name: str) -> None:
        """
        Set Label for this shape
        @param name: Str representing this shape
        @return: None
        """
        self.__name = name


class Rectangle(GeometricShape):
    def __init__(self, length: float, width: float):
        """
        Object representing a rectangle
        @param length: Float of length
        @param width: Float of width
        """
        super().__init__('Rectangle')
        self.set_length(length)
        self.set_width(width)

    def get_area(self):
        return self.get_length() * self.get_width()

    def get_perimeter(self):
        """
        Returns perimeter of this rectangle
        attribute length * width
        @return float self.length * self.width  
        """
        return 2 * self.get_length() + 2 * self.get_width()

    def get_length(self) -> float:
        return self.__length

    def set_length(self, length) -> None:
        self.__length = length

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width) -> None:
        self.__width = width


class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)
        super().__init__(side, side)
        self.set_name('Square')

    def set_side(self, side):
        self.set_width(side)
        self.set_length(side)
        self.__side = side

    def get_side(self):
        return self.__side

class Ellipse(GeometricShape):
    def __init__(self, semi_major_axis: float, semi_minor_axis: float) -> None:
        super().__init__("Ellipse")
        self.set_semi_major_axis(semi_major_axis)
        self.set_semi_minor_axis(semi_minor_axis)

    def get_perimeter(self) -> float:
        perimeter = pi * (3 * (self.get_semi_major_axis() + self.get_semi_minor_axis())
                          - sqrt((3 * self.get_semi_major_axis() + self.get_semi_minor_axis())
                                 * (self.get_semi_major_axis() + 3 * self.get_semi_minor_axis())))
        return perimeter

    def get_area(self) -> float:
        return self.get_semi_major_axis() * self.get_semi_minor_axis() * pi

    def get_semi_major_axis(self) -> float:
        return self.__semi_major_axis

    def set_semi_major_axis(self, semi_major_axis: float) -> None:
        self.__semi_major_axis = semi_major_axis

    def get_semi_minor_axis(self) -> float:
        return self.__semi_minor_axis

    def set_semi_minor_axis(self, semi_minor_axis: float) -> None:
        self.__semi_minor_axis = semi_minor_axis


class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)

        def set_radius(radius_):
            self.__radius = radius_

        set_radius(radius)
        self.set_name("Circle")

    def set_radius(self, radius):
        self.set_semi_major_axis(radius)
        self.set_semi_minor_axis(radius)
        self.__radius = radius


    def get_radius(self):
        return self.__radius