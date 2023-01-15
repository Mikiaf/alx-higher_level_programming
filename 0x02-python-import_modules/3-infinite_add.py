#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    result = 0
    for x in range(1, count):
        result += int(sys.argv[x])
print(result)
