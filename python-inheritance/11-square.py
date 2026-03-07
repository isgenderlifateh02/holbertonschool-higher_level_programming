#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
It includes a specific string representation for Square.
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
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        Format: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
