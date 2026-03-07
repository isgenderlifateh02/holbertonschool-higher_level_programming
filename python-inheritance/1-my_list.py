#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It provides an additional method to print the list in a sorted manner.
"""


class MyList(list):
    """
    MyList is a subclass of list that adds a custom sorting print method.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted in ascending order.
        Assumes all elements in the list are integers.
        """
        print(sorted(self))
