#!/usr/bin/python3
""" Add items in a list """

from os import path
from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    """
    # Adds all arguments to a Python list, and then save them to a file.
    """

    new_list = []

    """ Check if file exists """
    if path.isfile("add_item.json"):
        new_list = load("add_item.json")

    new_list.extend(argv[1:])

    save(new_list, "add_item.json")
