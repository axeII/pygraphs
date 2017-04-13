""" Task name: race

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
import re
import math

"""
A: B(2), C(-3)
B+: C(3), D(-2)
C: B(-4), D(-3)
D: A(-4)
"""

def parse_data(data):
    parsed_teams = []
    special = []
    for line in data:
        node, edges = line.split(':')
        if len(node) > 1:
            special.append(node)
        node = node[0]
        edges = [(e.strip()[0],int(re.findall(r'-?\d+',e)[0])) for e in edges.split(',')]
        parsed_teams.append((node,edges))

    return (parsed_teams,special)

def solve_with_graph(sol_data, special_nodes):
    if sol_data:
        nodes = set()
        for solve in sol_data:
            nodes.add(solve[0])
        hm = pyg.HMGraph(list(nodes),True)
        for sol in sol_data:
            for edg in sol[1]:
                hm.insert_edge(sol[0],edg[0],edg[1])

        #hm.print_hashMap(sorted_ = True)
        return hm.cpm_long(sol_data[0][0],special_nodes)

def print_final(final_data):
    path = []
    first = list(filter(lambda x: x[1][0] == None, final_data.items()))[0]
    path.append(first[0])
    if final_data:
        while not len(path) == len(final_data.keys()):
            first = list(filter(lambda x: x[1][0] ==
                first[0],final_data.items()))[0]
            path.append(first[0])
    print("-".join(path),final_data[path[-1]][1])

if __name__ == "__main__":
    try:
        data,s_nodes = parse_data(pyp.get_input_data(False))
        answer = solve_with_graph(data, s_nodes)
        print_final(answer)
    except KeyboardInterrupt:
        pass
