""" Task name: grups2.py

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
    if data:
        pot_nodes, pot_params = (data[0][0].split(','),data[1:])
        for nodes in pot_params:
            team = nodes.split('-')
            team = [pyp.strip_param(member) for member in team]
            parsed_teams.append(team)

        return (pot_nodes, parsed_teams)
    return []

def solve_with_graph(sol_data):
    if sol_data:
        hm = pyg.HMGraph([sol.strip() for sol in sol_data[0]])
        for team in sol_data[1]:
            for dat in [(team[x],team[x+1]) for x in range(len(team)-1)]:
                hm.insert_edge(dat[0],dat[1])
                hm.insert_edge(dat[1],dat[0])
        hm.print_hashMap()
    return None

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

