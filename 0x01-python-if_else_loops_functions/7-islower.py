#!/usr/bin/python3
def islower(c):
    if 122 >= ord(c) >= 97:
        return True
    else:
        return False
print("{}".format("lower"if (True) else "upper"))