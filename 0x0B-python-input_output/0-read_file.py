#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """read a text  file and print """
    with open(filename, 'r') as file_:
        print(file_.read(), end="")
    file_.close()
