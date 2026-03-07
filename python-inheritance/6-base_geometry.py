#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """
        Public instance method that raises an Exception.
        Message: area() is not implemented.
        """
        raise Exception("area() is not implemented")
