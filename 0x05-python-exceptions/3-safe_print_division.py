#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        code_working = True
        quotient = a / b
        return quotient
    except (ZeroDivisionError, TypeError):
        code_working = False
        return None
    finally:
        if code_working:
            print("Inside result: {}".format(quotient))
        else:
            print("Inside result: {}".format(None))
