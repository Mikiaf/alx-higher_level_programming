#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if (sys.argv[2] == '+' or sys.argv[2] == '-' or sys.argv[2] == '*' or sys.argv[2] == '/'):
        if sys.argv[2] == '+':
            print(add(int(sys.argv[1]), int(sys.argv[3])))
        elif sys.argv[2] == '-':
            print(sub(int(sys.argv[1]), int(sys.argv[3])))
        elif sys.argv[2] == '*':
            print(mul(int(sys.argv[1]), int(sys.argv[3])))
        elif sys.argv[2] == '/':
            print(div(int(sys.argv[1]), int(sys.argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
