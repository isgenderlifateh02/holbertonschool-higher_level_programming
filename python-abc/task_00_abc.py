#!/usr/bin/python3
"""
This module defines an abstract class Animal and its subclasses
Dog and Cat using the abc module.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class Animal.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """

    def sound(self):
        """Returns the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """

    def sound(self):
        """Returns the sound a cat makes."""
        return "Meow"
