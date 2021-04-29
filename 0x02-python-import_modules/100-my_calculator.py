#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operand = argv[2]

    if operand == "+":
        result = add(a, b)
    elif operand == "-":
        result = sub(a, b)
    elif operand == "*":
        result = mul(a, b)
    elif operand == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operand, b, result))
