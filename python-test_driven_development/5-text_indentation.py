#!/usr/bin/python3
"""prints text"""


def text_indentation(text):
    """func"""
    for i in text:
        if i == "." or i == "?" or i == ":" :
            if i != text[-1]:
                print(i + "\n\n")
        else:
            print(i, end="")
