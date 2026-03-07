#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj's class is a subclass of a_class and not a_class itself,
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
