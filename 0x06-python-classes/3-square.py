#!/usr/bin/python3

class Square:

    def __int__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self.__size = size

    def area(self):
        return self.__size * self.__size