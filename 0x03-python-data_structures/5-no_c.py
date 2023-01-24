#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if ord(i) == ord('c'):
            continue
        print("{}".format(i), end='')
