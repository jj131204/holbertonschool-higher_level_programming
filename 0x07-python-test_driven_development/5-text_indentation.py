#!/usr/bin/python3
""" function that prints a text with 2 new lines after
    each of these characters: ., ? and :
"""


def text_indentation(text):
    """Delimiters: '.', '?', ':'"""

    delimiters = [".", ":", "?"]
    i = 0

    if type(text) != str:
        raise TypeError("text must be a string")

    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in delimiters:
            print("\n")
            try:
                if text[i + 1] == " ":
                    while text[i + 1] == " ":
                        i += 1
            except Exception:
                pass
        i += 1
