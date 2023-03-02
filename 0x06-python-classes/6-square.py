#!/usr/bin/python3

class Square:
    def __init__(self,size=0, position=(0,0)):
        self.__size = size
        self.__position = position
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self,value):
        if not isinstance(value, tuple()) or len(value) > 1 or 