#!/usr/bin/python3
"""This is '0-read_file' module"""


def append_write(filename="", text=""):
    """Opens file, reads it and prints to stdout"""

    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
