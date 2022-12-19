#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if my_list_2 is None:
        my_list_2 = []
    if my_list_1 is None:
        my_list_1 = []
    list_result = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            list_result.append(result)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            list_result.append(0)
            print("division by 0")
        except IndexError:
            list_result.append(0)
            print("out of range")
        finally:
            pass
    return list_result
