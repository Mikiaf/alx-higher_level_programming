#!/usr/bin/python3
class list:
    def __init__(self):
        self.list = []
    def append(self,value):
        self.list.append(value)
    mylist = self.list
class MyList(list):
    def print_sorted(self):
        print(list.mylist)
