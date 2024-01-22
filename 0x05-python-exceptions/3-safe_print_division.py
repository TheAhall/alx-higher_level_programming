#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
        print("Inside result: {}".format(quotient))
        return quotient
    except (ZeroDivisionError, TypeError):
        print("Inside result: {}".format(None))
        return None
