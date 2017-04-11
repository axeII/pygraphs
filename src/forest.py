""" Task name: forest

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
    #hm.print_hashMap(sorted_=True)

    return (hm.travelling_salesman().get_edges(),hm.get_edges())

def print_final(final_data,graph_data):

    def getNum(data_,search_data):
        data = data_.split('-')
        accumulator = 0
        for d in range(len(data)-1):
            find = [dat for dat in search_data if dat[0] == data[d] and
                    dat[1][0] == data[d+1]][0]
            accumulator += find[1][1]
        return accumulator

    if final_data and graph_data:
            check_data = final_data[:]
            vertex = check_data.pop(0)
            graph = "%s-%s" % (vertex[0],vertex[1])
            while check_data:
                for vert in check_data:
                    if vert[0] == graph[-1]:
                        graph+= "-%s" % vert[1]
                        check_data.remove(vert)
                    elif vert[1] == graph[0]:
                        graph = "%s-%s" % (vert[0],graph)
                        check_data.remove(vert)
                    else:
                        continue
            print(graph,getNum(graph,graph_data))
if __name__ == "__main__":
    try:
            data = parse_data(pyp.get_input_data(False))
            answer, numbers = solve_with_graph(data)
            print_final(answer,numbers)
    except KeyboardInterrupt:
        pass
