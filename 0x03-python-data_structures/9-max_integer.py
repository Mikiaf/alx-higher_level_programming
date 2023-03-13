#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)
    x = 0
    if count == 0:
        return None
    else:
        while x < count:
            if my_list[x] > my_list[x + 1]:
                return my_list[x]
            x +=1 