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
                hm.insert_edge(val[1],val[0],'0',key+'_')
            #hm.print_hashMap()
            return (hm.edmons_karp(),hm)

def print_final(final_data,max_size,hm):
    if final_data:
        print('Grup size: %s' % final_data[0])

        past = sorted(list(filter(lambda x: x[2][-1] !=
            '_',reduce(list.__add__,hm.hashmax.values()))),key = lambda
            g:g[2])
        future = sorted(list(filter(lambda x: x[2][-1] !=
            '_',reduce(list.__add__,final_data[1].values()))),key = lambda
            g:g[2])

        for data1, data2 in zip(past,future):
            print('%s: %d' % (data1[2],data1[1]-data2[1]),"!" if data2[1] == 0 else
                    "")
        print('Time: ',int(max_size/final_data[0]) +
                (max_size % final_data[0] > 0) +
                final_data[2][2])
    else:
        print("Error graf se nepodarilo unikovou chodbu")

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data())
        final_data, graph_data = solve_with_graph(data)
        print_final(final_data,int(data[0][1]),graph_data)
    except KeyboardInterrupt:
        pass
