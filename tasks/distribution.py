""" Task name: distribution

Paste info about this task here, remeber to write what code is about.
"""

__author__ = 'Ales Lerch'

# Importing specific library

if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')

import os
import sys
from pygraphs import *

