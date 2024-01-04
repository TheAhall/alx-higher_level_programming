#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    sum_string = "{} + {} = {}".format(a, b, add(a, b))
    print(sum_string)
