#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    A square is a special case of a rectangle with equal sides.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.

        Note:
            size is validated by integer_validator from BaseGeometry.
            It is stored as a private attribute __size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
