#!/usr/bin/python3
""" function that prints a text with 2 new lines after
    each of these characters: ., ? and :
"""


def text_indentation(text):
    """Delimiters: '.', '?', ':'"""

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ('.', '?', ':'):
            print("{}\n".format(text[i]))
            if i + 1 < len(text):
                while text[i + 1] == " ":
                    i += 1
        else:
            print(text[i], end='')
        i += 1
