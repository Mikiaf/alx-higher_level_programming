#!/usr/bin/python3
"""defines Square"""


class Square:
    """repersents square"""

    def __init__(self, size=0):
        """
        agr:size represent size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        arg:value represents size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for x in range(self.__size):
            for y in range(self.__size):
                print('#', end='')
            print('\n')
