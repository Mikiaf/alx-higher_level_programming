#!/usr/bin/python3

def uppercase(str):
    for x in str:
        if 122>= ord(x) >= 97:
            x = ord(x) - 32
            print("{:c}".format(x),end='')
        else:
            print("{}".format(x),end='')
