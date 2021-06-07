#!/usr/bin/python3
"""
from_json_string
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python) represented by JSON str
    """
    return json.loads(my_str)
