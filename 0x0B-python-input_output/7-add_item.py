#!/usr/bin/python3
""" Add items in a list """

from os import path
from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def add_items():
    """
    # Adds all arguments to a Python list, and then save them to a file.
    """

    new_list = []

    """ Check if file exists """
    if path.isfile("add_item.json"):
        new_list = load("add_item.json")

    if len(argv) > 1:

        for i in range(1, len(argv)):
            new_list.append(argv[i])

    """ Write the list with the new elements in the file """
    save(new_list, "add_item.json")


if __name__ == "__main__":
    add_items()
