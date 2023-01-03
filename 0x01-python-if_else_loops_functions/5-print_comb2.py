#!/usr/bin/python3
for x in range(0, 100):
    if x > 9:
        print('{}'.format(x), end=', ')
    else:
        print('0{}'.format(x),end=', ')