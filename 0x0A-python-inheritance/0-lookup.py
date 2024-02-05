#!/usr/bin/python3
'''Lookup method'''


def lookup(obj):
    '''attributes and methods of an object
    Args:
    obj: the object to list

    Returns:
        list: the list of attributes
    '''
    return dir(obj)
