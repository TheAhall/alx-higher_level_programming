#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newlist = list(a_dictionary.keys())
    newlist.sort()
    for i in newlist:
        print("{}: {}".format(i, a_dictionary.get(i)))
