""" Task name: distribution

Paste info about this task here, remeber to write what code is about.
"""

__author__ = 'Ales Lerch'

# Importing specific library

import os
import sys

if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')

from graph_lib.pygraphs import *

