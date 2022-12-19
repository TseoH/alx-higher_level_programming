#!/usr/bin/python3

def safe_print_integer(value):
    printed = True
    try:
        parsed_value = int(value)
        print("{:d}".format(parsed_value))
    except:
        printed = False
    return printed
