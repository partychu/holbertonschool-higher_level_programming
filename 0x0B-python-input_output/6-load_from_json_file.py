#!/usr/bin/python3
"""
load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    creates obj from JSON file
    """
    with open(filename, 'r') as f:
        return json.load(f)
