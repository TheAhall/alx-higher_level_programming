#!/usr/bin/python3
'''Module for is_same_class'''


def is_same_class(obj, a_class):
    ''' checks if it s the same class'''
    if type(obj) == a_class:
        return True
    return False
