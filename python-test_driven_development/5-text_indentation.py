#!/usr/bin/python3
"""prints text"""


def text_indentation(text):
    """func"""
    for i in text:
        if i == "." or i == "?" or i == ":" :
            print(i + "\n\n")
        else:
            print(i, end="")
