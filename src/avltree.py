""" Task name: avltree

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


import graph_lib.pyparse as pyp
import graph_lib.pygraphs as pyg
import graph_lib.pyavltree as pya

def parse_data(data):
    return [pyp.strip_param(node) for node in data]

def solve_with_graph():
    pass

def print_final():
    pass

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data(False))
        print(data)
        #answer = solve_with_graph(data)
        #print_final(answer)
    except KeyboardInterrupt:
        pass
