#!/usr/bin/python3
"""This is '0-read_file' module"""


def write_file(filename="", text=""):
    """Opens file, reads it and prints to stdout"""

    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
