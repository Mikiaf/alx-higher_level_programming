#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    count = len(sys.argv)
    if count > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif ord(sys.argv[2]) == ord('+') or ord(sys.argv[2]) == ord('-') or ord(sys.argv[2]) == ord('*') or ord(sys.argv[2]) == ord('/'):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)