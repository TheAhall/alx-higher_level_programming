#!/usr/bin/python3
'''load_from_json_file module'''

import json


def load_from_json_file(filename):
    '''load_from_json_file:
        function that creates an Object from a “JSON file”
    '''
    with open(filename, mode='r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)
