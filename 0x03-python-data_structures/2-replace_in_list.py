#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if len(my_list) < idx:
        return my_list
    else:
        my_list[idx] = element
        return my_list