#!/usr/bin/python3

"""File json function"""


class Student:
    """Code here"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Code here 3"""
        return self.__dict__
