from math import pi, sqrt
import utils


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

        utils.validate_non_empty_string(name)

        self.__name = name

    def get_perimeter(self):
        raise NotImplementedError("Must specify a type of geometric shape to get perimeter")

    def get_area(self):
        raise NotImplementedError("Must specify a type of geometric shape to get area")


class Rectangle(GeometricShape):
    def __init__(self, length: [float, int], width: [float, int]):
        """
        Object representing a rectangle
        @param length: Float of length
        @param width: Float of width
        """
        super().__init__('Rectangle')
        self.set_length(length)
        self.set_width(width)

    def set_length(self, length) -> None:
        utils.validate_positive_number(length)

        self.__length = length

    def set_width(self, width) -> None:
        utils.validate_positive_number(width)

        self.__width = width

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

    def get_width(self) -> float:
        return self.__width


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.set_name('Square')

    def set_side(self, side):
        self.set_width(side)
        self.set_length(side)

    def get_side(self):
        return super().get_length()


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
        utils.validate_positive_number(semi_major_axis)
        self.__semi_major_axis = semi_major_axis

    def get_semi_minor_axis(self) -> float:
        return self.__semi_minor_axis

    def set_semi_minor_axis(self, semi_minor_axis: float) -> None:
        utils.validate_positive_number(semi_minor_axis)
        self.__semi_minor_axis = semi_minor_axis


class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.set_name("Circle")

    def set_radius(self, radius):
        self.set_semi_major_axis(radius)
        self.set_semi_minor_axis(radius)

    def get_radius(self):
        return super().get_semi_major_axis()


class ComplexShape(GeometricShape):
    def __init__(self, base: GeometricShape, holes):
        super().__init__('ComplexShape')
        self.set_holes(holes)
        self.set_base(base)

    def add_hole(self, hole: GeometricShape):
        self.get_holes().append(hole)

    def remove_hole(self, hole: GeometricShape):
        self.get_holes().remove(hole)

    def set_holes(self, holes: list):
        self.__holes = holes

    def get_holes(self) -> list:
        return self.__holes

    def get_edge_length(self):
        total_edge_length = self.get_base().get_perimeter()
        for hole in self.get_holes():
            total_edge_length += hole.get_perimeter()
        return total_edge_length

    def get_area(self):
        total_area = self.get_base().get_area()
        for hole in self.get_holes():
            total_area -= hole.get_area()
        return total_area

    def set_base(self, base: GeometricShape):
        self.__base = base

    def get_base(self) -> GeometricShape:
        return self.__base
