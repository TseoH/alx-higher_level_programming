#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    names = dir(hidden_4)
    names_len = len(names)

    for i in range(names_len):
        if names[:2] != '__':
            print("{}".format([names]))
