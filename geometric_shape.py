class GeometricShape:
    def __init__(self, name: str) -> None:
        """
        Parent class for Geometric Shapes
        @param name: Label for this shape
        """
        self.name = name

    @property
    def name(self) -> str:
        """
        Get Label for this shape
        @return: Label for this shape
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Set Label for this shape
        @param name: Str representing this shape
        @return: None
        """
        self._name = name


class Rectangle(GeometricShape):
    def __init__(self, length: float, width: float):
        """
        Object representing a rectangle
        @param length: Float of length
        @param width: Float of width
        """
        super().__init__('rectangle')
        self.length = length
        self.width = width

    def get_perimeter(self) -> float:
        """
        Returns perimeter of this rectangle
        attribute length * width
        @return float self.length * self.width  
        """
        return self.length * self.width

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length) -> None:
        self._length = length

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width) -> None:
        self._width = width


class Ellipse(GeometricShape):
    def __init__(self, semi_major_axis: float, semi_minor_axis: float) -> None:
        super().__init__("ellipse")
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    @property
    def semi_major_axis(self) -> float:
        return self._semi_major_axis

    @semi_major_axis.setter
    def semi_major_axis(self, semi_major_axis: float) -> None:
        self._semi_major_axis = semi_major_axis

    @property
    def semi_minor_axis(self) -> float:
        return self._semi_minor_axis

    @semi_minor_axis.setter
    def semi_minor_axis(self, semi_minor_axis: float) -> None:
        self._semi_minor_axis = semi_minor_axis
