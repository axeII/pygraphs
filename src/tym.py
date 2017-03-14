""" Task name: tym

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

import graph_lib.pygraphs as pyg
import graph_lib.pyparse as pyp


pyp.get_input_data()

def parse_data(data):
	pass

def solve_with_graph():
	pass

def print_final():
	pass
