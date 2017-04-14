""" Task name: weakness

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
        (transist, project) = nodes.split(':')
        parsed_teams.append(
                ([pyp.strip_param(member) for member
                    in transist.split('-')],project)
            )

    return parsed_teams

def solve_with_graph(sol_data):
    nodes = set()
    for solve in sol_data:
        for node in solve[0]:
            nodes.add(node)
    hm = pyg.HMGraph(list(nodes))
    for sol in sol_data:
        hm.insert_edge(sol[0][0],sol[0][1])
        hm.insert_edge(sol[0][1],sol[0][0])
    #hm.print_hashMap()
    if not hm.is_united():
        sys.exit(0)
    return hm.find_bridge(hm.find_articulation())

def print_final(final_data):
    if final_data and isinstance(final_data,dict):
        for key, val in final_data.items():
            for edge, value in val.items():
                if not value:
                    print('%s - %s' % (key,edge))
            print(key)

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data(False))
        answer = solve_with_graph(data)
        print_final(answer)
    except KeyboardInterrupt:
        pass
