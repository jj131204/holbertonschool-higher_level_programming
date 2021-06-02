#!/usr/bin/python3
"""write a class MyList that inherits from list:"""


class MyList(list):
    """class My_list"""

    def __init__(self):
        """ def __init__(self):"""
        super().__init__()

    def print_sorted(self):
        """def print_sorted(self):"""
        print(sorted(self))
