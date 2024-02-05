#!/usr/bin/python3
'''The Class MyList'''


class MyList(list):
    '''creating the class MyList'''
    def print_sorted(self):
        '''printing the sorted list'''
        sorted_list = sorted(self)
        print(sorted_list)
