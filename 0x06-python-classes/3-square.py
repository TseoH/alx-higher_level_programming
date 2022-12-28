#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square"""
    def __int__(self, size=0):
        """Initialize Square Instance
        Args:
            size (int): Square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self.__size = size

    def area(self):
        """
        Méthode qui retourne l'aire du carré.

        Returns :
            int : l'aire du carré.
        """
        return self.__size * self.__size
