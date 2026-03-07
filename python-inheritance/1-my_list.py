#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList is a subclass of list with a sorting method.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements are integers.
        """
        print(sorted(self))
