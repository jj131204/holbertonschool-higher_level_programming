#!/usr/bin/python3
""" function that writes a string to a text file (UTF8)
 and returns the number of characters written"""


def write_file(filename="", text=""):
    """write a  string and returns the number of characters"""

    with open(filename, 'w') as file_:

        file_.write(text)
        return len(text)
    file_.close()
