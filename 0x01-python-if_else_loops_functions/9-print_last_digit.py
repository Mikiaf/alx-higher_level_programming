#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        i = abs(number) % i
    else:
        i = number % 10
    print("{}".format(i), end='')
    return abs(i) % 10
