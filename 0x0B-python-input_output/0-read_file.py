#!/usr/bin/python3
'''Define read file module'''


def read_file(filename=""):
    '''read_file: function that reads a text file'''
    with open(filename, mode='r', encoding="utf-8") as myfile:
        print(myfile.read(), end='')
