""" Task name: grups

Paste info about this task here, remeber to write what code is about.
"""

__author__ = 'Ales Lerch'

import os
import sys

#Importing specific library

if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')

from graph_lib.pygraphs import *

def strip_param(param):
        return param.strip().replace('\n','')

def get_input_data():
    pole = []
    for line in fileinput.input():
        if fileinput.isfirstline():
            pole.append([strip_param(line)])
        else:
            pole.append(strip_param(line))
    return pole

def parse_data(data):
    parsed_data = []
    arg = data[0]
    params = data[1:]
    for par in params:
        (car, rest) = par.split(':')
        places = rest.split('>')
        places = [strip_param(x) for x in places]
        parsed_data.append((car,places))

    print(parsed_data)
    return parsed_data

def solve_with_graph():
    pass

def print_final():
    pass

