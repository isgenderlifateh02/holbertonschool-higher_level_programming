#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
The class provides a foundation for geometry-related objects
with methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometry shapes.
    It includes methods for calculating area and validating integers.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        The message of the exception is 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the 'value' parameter.
        The 'name' is assumed to be a string.
        The 'value' must be a positive integer greater than 0.

        Args:
            name (str): The name associated with the value.
            value (int): The integer value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
