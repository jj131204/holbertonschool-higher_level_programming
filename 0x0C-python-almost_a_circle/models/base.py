#!/usr/bin/python3
"""create class Base"""
import json


class Base:
    """class  base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ def __init__(self, id=None): """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
            
        return json.dumps(list_dictionaries)
