#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a class, or an instance of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance or inherited from a_class, else False.
    """
    return isinstance(obj, a_class)
