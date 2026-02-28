#!/usr/bin/python3
"""Düzbucaqlı sinfini təyin edən modul"""


class Rectangle:
    """Düzbucaqlını təmsil edən sinif"""

    def __init__(self, width=0, height=0):
        """Yeni düzbucaqlı obyekti yaradır"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni oxumaq üçün getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin etmək üçün setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü oxumaq üçün getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin etmək üçün setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
