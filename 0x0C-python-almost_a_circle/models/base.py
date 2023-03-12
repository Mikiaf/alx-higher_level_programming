#!/usr/bin/python3
"""define class called Base"""

class Base:
    """define privite class attribute called __nb__objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects