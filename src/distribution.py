""" Task name: distribution

Paste info about this task here, remeber to write what code is about.
"""

__author__ = 'Ales Lerch'

# Importing specific library

import os
import sys

if os.path.isdir('./lib'):
    sys.path.append('./lib')
else:
    sys.path.append('../lib')

import graph_lib.pyparse as pyp
import graph_lib.pygraphs as pyg

def parse_data(data):
    parsed_data = []
    (arg,params) = (data[0],data[1:])
    arg = arg[0].split(',')
    for par in params:
        (car, rest) = par.split(':')
        places = rest.split('>')
        places = [pyp.strip_param(x) for x in places]
        parsed_data.append((car,places))

    return (arg,parsed_data)

def solve_with_graph(sol_data):
    hm = pyg.HMGraph(sol_data[0])
    for auto,places in sol_data[1]:
        for dat in [(places[x],places[x+1]) for x in range(len(places)-1)]:
            #print(dat,dat[0],dat[1])
            hm.insert_edge(dat[0],dat[1])

    final = {}
    (final['place'],final['count']) = hm.find_most_used_node()
    final['connection'] = hm.double_round
    final['warehouse'] = hm.has_cycle()

    return final

def print_final(final_data):
    if final_data:
        print("nejvice navstevovany: %s %i" %
                (final_data['place'],final_data['count']))
        print("existuje vice spojeni: %s" %
                'ano' if final_data['connection'] else 'ne')
        print("zbozi zpet do skladu: %s" %
                'ano' if final_data['warehouse'] else 'ne')

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data())
        final_data = solve_with_graph(data)
        print_final(final_data)
    except KeyboardInterrupt:
        pass
