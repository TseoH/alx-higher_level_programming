#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    if roman_string is None:
        return num
    for i in range(len(roman_string)):
        if roman_numerals.get(roman_string[i], 0) == 0:
            return num
        if (i != (len(roman_string) - 1) and
                roman_numerals[roman_string[i]] < roman_numerals[roman_string[i + 1]]):
            num += roman_numerals[roman_string[i]] * -1
        else:
            num += roman_numerals[roman_string[i]]
    return num
