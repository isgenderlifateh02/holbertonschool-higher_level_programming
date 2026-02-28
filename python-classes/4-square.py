#!/usr/bin/python3
"""Module that defines a Square class with getter and setter"""


class Square:
    """Class that represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return (self.__size ** 2)
