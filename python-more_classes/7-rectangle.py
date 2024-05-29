#!/usr/bin/python3
"""Module rect class"""


class Rectangle:
    """rect class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes object"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """returns presentation of rectangle using # chars"""
        rect = ""
        if 0 in {self.width, self.height}:
            return rect

        for i in range(self.height):
            rect += self.print_symbol * self.width + ("\n" if i != self.height - 1 else "")
        return rect

    def __repr__(self):
        """returns presentation of rectangle using # chars"""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """returns presentation of rectangle using # chars"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """function"""
        return self.__width

    @width.setter
    def width(self, value):
        """function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """function"""
        return self.__height

    @height.setter
    def height(self, value):
        """function"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
