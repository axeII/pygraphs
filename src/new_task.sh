#!/bin/bash

INFO="Paste info about this task here, remeber to write what code is about."
AUTHOR="__author__ = \'Ales Lerch\'"

TEXT="import os
import sys\n
#Importing specific library\n
if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')\n
from graph_lib.pygraphs import *\n\n"

FUNCTIONS="def get_input_data():\n\tpass
def parse_data(data):\n\tpass\n
def solve_with_graph():\n\tpass\n
def print_final():\n\tpass\n"

for file in $@ ; do
	NAME="$file.py" ;
	touch $NAME ;
	printf "\"\"\" Task name: $file\n\n" > $NAME ;
	printf "$INFO\n\"\"\"\n\n" >> $NAME ;
	printf "$AUTHOR\n\n" >> $NAME ;
	printf "$TEXT" >> $NAME ;
	printf "$FUNCTIONS" >> $NAME ;
	printf "Generated $NAME file\n"
done
