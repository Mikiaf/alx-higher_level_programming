#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if ord(i) == ord('c') or ord(i) == ord('C'):
            continue
        new_string += i
    return new_string
