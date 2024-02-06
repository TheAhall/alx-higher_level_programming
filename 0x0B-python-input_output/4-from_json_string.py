#!/usr/bin/python3
'''Define from_json_string module'''

import json


def from_json_string(my_str):
    ''' from_json_string:
        a function that returns an object represented by a JSON string
    '''
    return json.loads(my_str)
