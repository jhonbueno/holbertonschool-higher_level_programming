#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    len = len(argv) - 1

    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    b = int(args[3])
    operator = args[2]

    if operator == "+":
        result = add(a, b)
        print("{} {} {} = {}".format(a, operator, b, result)
    elif operator == "-":
        result = sub(a, b)
        print("{} {} {} = {}".format(a, operator, b, result)
    elif operator == "*":
        result = mul(a, b)
        print("{} {} {} = {}".format(a, operator, b, result)
    elif operator == "/":
        result = div(a, b)
        print("{} {} {} = {}".format(a, operator, b, result)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)