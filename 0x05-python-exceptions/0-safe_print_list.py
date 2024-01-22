#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indexsum = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            break
        indexsum += 1
    print()
    return indexsum
