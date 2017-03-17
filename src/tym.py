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


import graph_lib.pyparse as pyp
import graph_lib.pygraphs as pyg

def parse_data(data):
    parsed_teams = []
    for nodes in data:
        (team, project) = nodes.split(':')
        team = team.split('-')
        team = [pyp.strip_param(member) for member in team]
        parsed_teams.append(team)

    return parsed_teams

def solve_with_graph(sol_data):
    nodes = set()
    [nodes.update(nod) for nod in [sol for sol in sol_data]]
    hm = pyg.HMGraph(list(nodes))
    for sol in sol_data:
        hm.insert_edge(sol[0],sol[1])
        hm.insert_edge(sol[1],sol[0])
    #hm.print_hashMap()
    clique = hm.find_clique()

    return clique

def print_final(final_data):
    if final_data:
        for data in final_data:
            print(", ".join(data))

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data(False))
        cli = solve_with_graph(data)
        print_final(cli)
    except KeyboardInterrupt:
        pass
