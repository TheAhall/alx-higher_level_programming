#!/usr/bin/python3
'''Define append_write modul'''


def append_write(filename="", text=""):
    '''
    append_write:
        function that appends a string at the end of a text file
    '''
    with open(filename, mode='a', encoding='utf-8') as myfile:
        return myfile.write(text)
