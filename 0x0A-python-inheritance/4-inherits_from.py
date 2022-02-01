#!/usr/bin/python3
"""function that returns True if the object is an instance of a class """


def inherits_from(obj, a_class):
    """Return if is a subclass"""
    return issubclass(type(obj), a_class)
