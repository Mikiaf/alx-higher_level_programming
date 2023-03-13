#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        new_list = []
        for x in my_list:
            if x != my_list[idx]:
                new_list.append(x)
        my_list.remove(my_list[idx])
        return new_list