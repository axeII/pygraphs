""" Task name: grups

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

def parse_data(data):
    parsed_teams = []
    (pot_nodes,pot_params) = (data[0].split(','),data[1:])
    for nodes in pot_params:
        team = rest.split('-')
        team = [pyp.strip_param(x) for member in team]
        parsed_data.append(team)

    return (pot_nodes,parsed_teams)

def solve_with_graph(sol_data):
    hm = pyg.HMGraph(sol_data[0])
    for team in sol_data[1]:
        hm.insert_edges(team)

    biparted = hm.is_biparted()
    return [map(lambda barva :[x for x,y in biparted.items() if y ==
        barva],"cervena","zelena")]

def print_final(final_data):
    if final_data:
        for nodes in final_data:
            print(nodes)
    else:
        print("Nelze rozdelit.")

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data())
        final_data = solve_with_graph(data)
        print_final(final_data)
    except KeyboardInterrupt:
        pass
