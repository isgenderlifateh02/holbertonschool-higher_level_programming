#!/usr/bin/python3
"""
This module defines the BaseGeometry class which serves as a base
for all geometry-related objects in this project. It includes
foundational methods that other shapes will inherit and implement.
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometry shapes. It provides
    common functionality for validating integers and serves as a
    blueprint for more specific geometric shapes like Rectangles.
    """

    def area(self):
        """
        Public instance method that calculates the area of the shape.
        Currently, this method is not implemented in the base class
        and must be overridden by any subclass that inherits from it.
        Raises:
            Exception: always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the 'value' parameter.
        It ensures that the value is a strictly positive integer.
        The 'name' is a string used for the error message if needed.
        Args:
            name (str): The name associated with the value being validated.
            value (int): The actual integer value that needs validation.
        Raises:
            TypeError: If the value provided is not a basic integer type.
            ValueError: If the value provided is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

