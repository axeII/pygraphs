""" Task name: evacuation

Paste info about this task here, remeber to write what code is about.
"""

__author__ = 'Ales Lerch'

import os
import sys
from functools import reduce

#Importing specific library

if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')


import graph_lib.pyparse as pyp
import graph_lib.pygraphs as pyg

def parse_data(data):
    parsed_paths = {}
    if data:
        first_node, node_params = (data[0][0].split(':'),data[1:])
        for node in node_params:
            door, room = node.split(':')
            room = [dr for dr in room.split(' ') if dr and dr != '>']
            parsed_paths[door] = room
        return (first_node, parsed_paths)
    return []

def solve_with_graph(sol_data):
    if sol_data:
        hm = pyg.HMGraph(sorted(list(set(reduce(list.__add__,[sol[:2] for sol
            in sol_data[1].values()],[])))),True,sol_data[0][0])
        if hm:
            for key, val in sol_data[1].items():
                hm.insert_edge(val[0],val[1],val[2],key)
                hm.insert_edge(val[1],val[0],'0',key)
            hm.print_hashMap()
            return (hm.edmons_karp(),hm)

def print_final(final_data,hm):
    if final_data:
        print('#'*77)
        for key, val in hm.hashmax.items():
            print(key,': ',val)
        print('#'*77)
        for key, val in final_data.items():
            print(key,': ',val)
    else:
        print("Error graf se nepodarilo unikovou chodbu")

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data())
        final_data,hm = solve_with_graph(data)
        print_final(final_data,hm)
    except KeyboardInterrupt:
        pass

