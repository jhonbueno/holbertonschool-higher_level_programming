#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry
class BaseGeometry(BaseGeometry):
    def area(self):
        raise Exception("area() is not implemented")

