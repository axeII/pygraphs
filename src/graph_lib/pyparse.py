""" Pyparse

This is modul for task parsing since most of the operations are same
"""

__author__ = 'Ales Lerch'

import os
import sys
import fileinput

def strip_param(param):
        return param.strip().replace('\n','')

def get_input_data(first_row_diffrent = True):
    """
    pokud je to prvni radek vloz jej do data_streamu jako pole jinak vkladej
    jako dalsi radky
    """
    data_stream = []
    for line in fileinput.input():
        if fileinput.isfirstline() and first_row_diffrent:
            data_stream.append([strip_param(line)])
        else:
            data_stream.append(strip_param(line))
    return data_stream

