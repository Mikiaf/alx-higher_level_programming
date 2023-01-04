#!/usr/bin/python3
def uppercase(str):
    for x in str:
        upper = ord(x) - 32
        print("{:c}".format(upper), end='')
uppercase("miki")