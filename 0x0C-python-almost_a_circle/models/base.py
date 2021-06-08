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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""

        str_ = []

        if list_objs is None or list_objs == []:
            str_ = "[]"
        else:
            name = cls.__name__ + ".json"

            for i in list_objs:
                str_.append(cls.to_dictionary(i))

            with open(name, mode="w") as file:
                file.write(cls.to_json_string(str_))
