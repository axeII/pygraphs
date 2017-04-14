""" Task name: reset

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
    hm = pyg.HMGraph(list(nodes),True)
    for sol in sol_data:
        hm.insert_edge(sol[0][0],sol[0][1],int(sol[1]))
        hm.insert_edge(sol[0][1],sol[0][0],int(sol[1]))
    #hm.print_hashMap()

    return hm.find_graph_skeleton()

def print_final(final_data):
    for data in final_data:
        field = sorted([data[0],data[1][0]])
        print('%s - %s: %s' %(field[0],field[1],data[1][1]))
    print('Hodnoceni:',sum([x[1][1] for x in final_data]))

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data(False))
        answer = solve_with_graph(data)
        print_final(answer)
    except KeyboardInterrupt:
        pass
