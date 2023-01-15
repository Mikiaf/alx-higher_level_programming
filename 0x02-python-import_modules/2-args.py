#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    arg = len(sys.argv) - 1
    print("{} arguments:".format(arg))
    for x in range(1, arg + 1):
        print("{}: {}".format(i, sys.argv[x]))
        i += 1
