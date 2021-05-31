#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """read a text  file and print """
    file_ = open(filename, 'r')

    print(file_.read(), end="")
