#!/usr/bin/python3
'''define save_to_json_file module'''

import json


def save_to_json_file(my_obj, filename):
    '''
    save_to_json_file:
        function that writes an Object to a text file, using a JSON representation
    '''
    with open(filename, mode='w', encoding='utf-8') as myfile:
        json.dump(my_obj, myfile, ensure_ascii=False)
