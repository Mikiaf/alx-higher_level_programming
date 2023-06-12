#!/usr/bin/python3
from models.base import Base
"""
defining rectangle class
thst inherit from Base class
"""


class Rectangle(Base):
    """
    Private instance attributes, 
    each with its own public getter and setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        """
        seting a getter and setter for widht
        """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
    """
    seting a getter and setter for height
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    """
    seting getter and setter for x
    """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    """
    seting getter and setter for y
    """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
