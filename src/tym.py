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

from graph_lib.pygraphs import *

def get_input_data():
	pass
def parse_data(data):
	pass

def solve_with_graph():
	pass

def print_final():
	pass
