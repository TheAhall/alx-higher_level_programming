#!/usr/bin/python3
'''Define write_file modul'''


def write_file(filename="", text=""):
    '''write_file: function that writes a string to a text file'''
    with open(filename, mode='w', encoding='utf-8') as myfile:
        return myfile.write(text)
