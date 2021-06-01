#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file:"""

from os import path
from sys import argv

save_to_json_file =__import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """
    # Adds all arguments to a Python list, and then save them to a file.
    """

    new_list = []

    """ Check if file exists """
    if path.isfile("add_item.json"):
        new_list = load_from_json_file("add_item.json")

    """
    try:
        new_list = create("add_item.json")
    except  FileNotFoundError:
        new_list = []
    """
    new_list.append(argv[1:])

    """ Write the list with the new elements in the file """
    save_to_json_file(new_list, "add_item.json")
