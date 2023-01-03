#!/usr/bin/python3

class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    number_of_instances (int): The number of Rectangle instances.
    print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle object.

        Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
        value (int): The new width of the rectangle.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
        int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
        value (int): The new height of the rectangle.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        """
        Get the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Get the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
        rect_1: An instance of Rectangle.
        rect_2: An instance of Rectangle.

        Returns:
        rect_1 if both have the same area value.
        Otherwise, returns the rectangle with the bigger area.

        Raises:
        TypeError: If rect_1 is not an instance of Rectangle.
        TypeError: If rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """
        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for i in range(self._height):
            [rect.append(str(self.print_symbol)) for _ in range(self._width)]
            if i != self._height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """
        Return the string representation of the Rectangle.
        """
        representation = "Rectangle(" + str(self._width)
        representation += ", " + str(self._height) + ")"
        return representation

    def __del__(self):
        """
        Deletion deletion.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
