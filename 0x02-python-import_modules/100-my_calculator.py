#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv[1:]
    arg_count = len(arg)
    operators = ["+", "-", "*", "/"]
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{:d} {} {:d} = {:d}".format(a, operators[0], b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{:d} {} {:d} = {:d}".format(a, operators[1], b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{:d} {} {:d} = {:d}".format(a, operators[2], b, mul(a, b)))
        elif sys.argv[2] == '/':
            print("{:d} {} {:d} = {:d}".format(a, operators[3], b, div(a, b)))
