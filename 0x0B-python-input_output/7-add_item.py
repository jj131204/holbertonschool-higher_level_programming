#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file:"""

from os import path
from sys import argv

if __name__ == "__main__":

    new_list = []

    write = __import__('5-save_to_json_file').save_to_json_file
    create = __import__('6-load_from_json_file').load_from_json_file

    if path.isfile("add_item.json"):
        new_list = load_from_json_file("add_item.json")

    """
    try:
        new_list = create("add_item.json")
    except  FileNotFoundError:
        new_list = []
    """
    new_list.append(argv[1:])

    write(new_list, "add_item.json")
