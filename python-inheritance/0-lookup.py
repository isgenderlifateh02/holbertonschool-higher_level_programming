#!/usr/bin/python3
"""
This module provides a function to list all attributes
and methods of an object.
"""
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
