#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for x in set_1:
        for y in set_2:
            if x == y:
                new_list.append(x)
    return new_list
