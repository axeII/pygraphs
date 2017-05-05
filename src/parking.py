""" Task name: parking

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
        for node in data:
            adress, space = node.split(':')
            adress, position = adress.split(' ')
            for fac in range(1,int(space)+1):
                parsed_paths["%s_%d" %(adress,fac)] = (adress,position,space)
        return parsed_paths
    return []

def solve_with_graph(sol_data):

    def count_metric(data,posA,posB):
        position1 = data[posA][1].split(',')
        position2 = data[posB][1].split(',')
        rho = abs(int(position1[0]) - int(position2[0])) +\
            abs(int(position1[1]) - int(position2[1]))
        return str(rho)

    if sol_data:
        hm = pyg.HMGraph(sorted(sol_data.keys()),True)
        if hm:
            #projet jenom baraky a nasmerovat je na parkoviste
            for key_b in list(filter(lambda s:s[0]=='B',sorted(sol_data.keys()))):
                for key_p in list(filter(lambda s:s[0]=='P',sorted(sol_data.keys()))):
                    hm.insert_edge(key_b,key_p,count_metric(sol_data,key_b,key_p))
                    hm.insert_edge(key_p,key_b,count_metric(sol_data,key_p,key_b))
            #hm.print_hashMap()
            return hm.paring_hungarian()
    return None

def print_final(final_data):
    count = 0
    if final_data:
        for k,val in final_data.items():
            count += val[1]
            print(val[0],val[1])
        print("Celkem: %d" % count)
    else:
        print("Error graf totall error")

if __name__ == "__main__":
    try:
        data = parse_data(pyp.get_input_data(False))
        final_data = solve_with_graph(data)
        print_final(final_data)
    except KeyboardInterrupt:
        pass
