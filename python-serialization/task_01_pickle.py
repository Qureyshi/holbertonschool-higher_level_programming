#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object"""

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """CustomObject or None if an error occurs"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None