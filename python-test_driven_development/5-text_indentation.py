#!/usr/bin/python3
"""prints text"""


def text_indentation(text):
    """func"""
    new_text = ""
    new_text = text.replace(". ", ".")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace("? ", "?")

    for i in text:
        if i == "." or i == "?" or i == ":" :
            if i != text[-1]:
                print(i)
                print("\n\n")
        else:
            print(i, end="")
    print("\n")
