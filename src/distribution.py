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

import fileinput
import graph_lib.pygraphs as pyg

def strip_param(param):
        return param.strip().replace('\n','')

def get_input_data():
    pole = []
    for line in fileinput.input():
        if fileinput.isfirstline():
            pole.append([strip_param(line)])
        else:
            pole.append(strip_param(line))
    return pole

def parse_data(data):
    parsed_data = []
    (arg,params) = (data[0],data[1:])
    arg = arg[0].split(',')
    for par in params:
        (car, rest) = par.split(':')
        places = rest.split('>')
        places = [strip_param(x) for x in places]
        parsed_data.append((car,places))

    return (arg,parsed_data)

def solve_with_graph(sol_data):
    #print(sol_data[0])
    pg = pyg.MaticeSousednosti(sol_data[0])
    for auto,places in sol_data[1]:
        print(auto,places)
    pg.vypisMS()

    return ""

def print_final(final_data):
    if final_data:
        print("nejvice navstevovany: %s %i" %
                (final_data['place'],final_data['num']))
        print("existuje vice spojeni: %s" %
                'ano' if final_data['exist_spoj'] else 'ne')
        print("zbozi zpet do skladu: %s" %
                'ano' if final_data['sklad'] else 'ne')

if __name__ == "__main__":
    try:
        data = parse_data(get_input_data())
        final_data = solve_with_graph(data)
        final_data = {'place': 'Test','num': 4,'exist_spoj': True,'sklad': True}
        #print_final(final_data)
    except KeyboardInterrupt:
        pass
