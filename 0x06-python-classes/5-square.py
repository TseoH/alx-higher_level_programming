#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square"""
    def __init__(self, size=0):
        """Initialize Square Instance
        Args:
            size (int): Square size
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Méthode qui retourne l'aire du carré.

        Returns :
            int : l'aire du carré.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print method"""
        for i in range(0, self.__size):
            [print("#", end="") for _x in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
