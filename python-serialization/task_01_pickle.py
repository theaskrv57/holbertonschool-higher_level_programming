#!/usr/bin/env python3
"""Serialize and deserialize a custom class using pickle."""
import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes."""

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize a CustomObject instance from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject or None: Returns the object or None if error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.PickleError, EOFError, IOError):
            return None
