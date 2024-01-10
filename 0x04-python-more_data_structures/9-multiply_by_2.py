#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    newlist = list(newdict.keys())
    for i in newlist:
        newdict[i] *= 2
    return newdict
