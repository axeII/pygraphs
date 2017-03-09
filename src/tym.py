""" Task name: tym

Paste info about this task here, remeber to write what code is about.
"""

__author__ = 'Ales Lerch'

#import os
import sys

Importing specific library

if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')

from graph_lib.pygraphs import *

