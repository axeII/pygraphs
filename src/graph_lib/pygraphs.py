""" Pygraphs

Graph library, this file should be splitted when goes bigger.
"""

__author__ = 'Ales Lerch'

import os
import sys
import pprint

class HMGraph:
    """
    Hash Matrix Graph implementation.
    """

    def create_node(node_id,node_name,node_count):
        new_node = {}
        new_node['element'] = node_id + 1
        new_node['node_name'] = node_name
        new_node['counting'] = node_count
        #new_node['next'] = None

        return new_node

    def __init__(self,setup_nodes):
        self.nodes = []
        self.edges = {}
        self.matrix = []
        for spec_node in range(len(setup_nodes)):
            self.matrix.append(HMGraph.create_node(spec_node,setup_nodes[spec_node],0))

    def add_node(self,name = ""):
        self.matrix.append(HMGraph.create_node(int(len(self.matrix)+1),name,0))

    def pop_node(self,which = None):
        if not which:
            self.matrix.pop()
        else:
            self.matrix.pop(which)

    def print_hashMatrix(self,order = None):
        """
        pokud je lepsi zpusob jak to vypast tak ho dat sem
        """
        pp = pprint.PrettyPrinter(indent=4)
        if order:
            for node in self.matrix:
                pp.pprint(node)
        else:
            pp.pprint(self.matrix)

    def get_nodes(self):
        self.nodes = [node['node_name'] for node in self.matrix]
        return self.nodes

    def get_edges(self):
        for node in self.nodes:
            self.edges[node] = [y for y in [x.keys() for x in self.matrix] if y
                    in self.nodes]
        self.edges = [node for node in self.matrix]
        return self.edges

    def insert_edges(self,data):
        """
        Je moznost tuto cast programu napsat recurziven tak ze pridam funci
        add_new_node kteoru pak volam pokud next neni prazdny jinak vloznim
        novy node do nextu.
        """
        search_name = data[0]
        search_que = data[1:]
        for element in self.matrix:
            if element['node_name'] == search_name:
                operative = element

        if operative:
            # pro zbytek v ceste
            for element_que in range(search_que):
                new_node = {}
                new_node['prvek'] = element_que + 1
                """
                celkem zbytecne kdyz je to klic ale muzu sem narvat
                dopravni prostredek napr misto repeat nazvu
                """
                new_node['node_name'] = search_que[element_que]
                new_node['counting'] = 1
                operative[search_que[element_que]] = new_node
        else:
            print('Error: No Node found')

class LinkedGraph:

    pass


class EdgeGraph:

    pass

if __name__ == "__main__":
    test1 = HMGraph([1,2,3])
    test1.print_hashMatrix()
