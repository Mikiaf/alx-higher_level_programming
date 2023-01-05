#!/usr/bin/python3

def uppercase(str):
    for x in str:
        if 122 >= ord(x) >= 97:
            x = chr(ord(x) - 32)
        print("{}".format(x),end='')
    print()
uppercase('Miki is the best')