#!/usr/bin/python3
"""This module Converts string object to JSON"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
