#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x == ord('e') or x == ord('q'):
        continue
    print('{:c}'.format(x), end="")
