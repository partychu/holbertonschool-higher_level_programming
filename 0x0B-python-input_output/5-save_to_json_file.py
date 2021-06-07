#!/usr/bin/python3
"""
save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an obj to a txt file using a JSON repr
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
