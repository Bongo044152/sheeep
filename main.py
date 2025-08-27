#!/usr/bin/env python3

import sys
from utils.arithmetic import add, sub, mul, div
from utils.temperature import c_to_f, f_to_c


HELP = """
Usage:
  python3 src/main.py <group> <cmd> [args...]

Groups & Commands:
  calc add a b -> a + b
  calc sub a b -> a - b
  calc mul a b -> a * b
  calc div a b -> a / b

  temp c2f c -> Celsius to Fahrenheit
  temp f2c f -> Fahrenheit to Celsius

Examples:
  python3 src/main.py calc add 3 5
  python3 src/main.py temp c2f 25
"""


def parse_number(s):
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        print(f"error: not a number -> {s}")
        sys.exit(1)


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help", "help"):
        print(HELP)
        return

    group = argv[1]
    if group == "calc":
        if len(argv) != 5:
            print("calc usage: python3 src/main.py calc <add|sub|mul|div> a b")
            return
        cmd, a_str, b_str = argv[2], argv[3], argv[4]
        a = parse_number(a_str)
        b = parse_number(b_str)

        if cmd == "add":
            print(add(a, b))
        elif cmd == "sub":
            print(sub(a, b))
        elif cmd == "mul":
            print(mul(a, b))
        elif cmd == "div":
            if b == 0:
                print("error: division by zero")
                return
            print(div(a, b))
        else:
            print("unknown calc command")

    elif group == "temp":
        if len(argv) != 4:
            print("temp usage: python3 src/main.py temp <c2f|f2c> value")
            return
        cmd, v_str = argv[2], argv[3]
        v = parse_number(v_str)

        if cmd == "c2f":
            print(c_to_f(v))
        elif cmd == "f2c":
            print(f_to_c(v))
        else:
            print("unknown temp command")

    else:
        print("unknown group; use 'calc' or 'temp' or --help")


if __name__ == "__main__":
    main(sys.argv)
