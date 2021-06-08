#!/usr/bin/python3
"""
Base module
"""
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static Method: JSON str repr"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Static Method: List of JSON str repr"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

#    @classmethod
#    def save_to_file(cls, list_objs):

#    @classmethod
#    def create(cls, **dictionary):

#    @classmethod
#    def load_from_file(cls):
