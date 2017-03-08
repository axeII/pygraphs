import os
import sys
# Importing specific library
if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')

from pygraphs import *

print("hello_world")
