#!/usr/bin/python3
"""class Student"""


class Student:
    """
    Write a class Student that defines a student by:
    Public instance attributes:
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or type(attrs) is not list:
            return self.__dict__

        else:
            dic_ = {}
            for x in self.__dict__:
                for y in attrs:
                    if x is y:
                        dic_[x] = self.__dict__[x]
            return dic_
