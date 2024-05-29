#!/usr/bin/python3
"""Module rect class"""

class Rectangle:
    """rect class"""

    def __init__(self, with = 0, height = 0):
        """Initializes object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """function"""
        return self.__width

    @with.setter
    def width(self, value):
        """function"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """function"""
        return self.__height

    @height.setter
    def height(self, value):
        """function"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
