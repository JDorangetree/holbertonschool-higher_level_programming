#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    def find_operator(c):
        operators = "+-/*"
        for i in range(0, 4):
            if operators[i] == c:
                return operators[i]
            else:
                pass
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = find_operator(sys.argv[2])
    if sign == "+":
        result = add(a, b)
        print("{}".format(result))
    elif sign == "-":
        result = sub(a, b)
        print("{}".format(result))
    elif sign == "*":
        result = mul(a, b)
        print("{}".format(result))
    elif sign == "/":
        result = div(a, b)
        print("{}".format(result))
