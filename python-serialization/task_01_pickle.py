#!/usr/bin/python3
"""
This module defines a CustomObject class and demonstrates
serialization using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """Initializes the custom object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a formatted way."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and deserializes an instance from a file.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
