#!/usr/bin/python3
"""This is a '5-save_to_json_file' module"""


import json


def load_from_json_file(filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as myfile:
        json.load(myfile)
