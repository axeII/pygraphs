""" Pygraphs

Graph library, this file should be splitted when goes bigger.
"""

__author__ = 'Ales Lerch'

import os
import sys
import pprint
import collections

"""
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
"""
class HMGraph:
    """
    Hash Matrix Graph implementation.
    """

    def __init__(self,setup_nodes = []):
        """
        Maybe different library for for hashmax if to include order key inputs if
        needed in this data structure
        data_dict = collections.OrderedDict(sorted(data_dict.items()))
        """
        self.hashmax = {}
        self.hashmax = collections.OrderedDict()
        self.double_round = False
        if setup_nodes and isinstance(setup_nodes,list):
            """
            In case to use indexes as int use range(len(setup_nodes))
            else let it as key name it's python
            """
            for spec_node in setup_nodes:
                self.hashmax[spec_node] = []
                #(HMGraph.create_node(spec_node,setup_nodes[spec_node],0))


    def add_node(self,name = "",edges = [], update = ()):
        if name and name not in self.hashmax.keys():
            if not edges:
                print("Info: No edges were inputed with node %s" % name)
            self.hashmax[name] = edges
        else:
            print('Error: Node: [%s] is alredy in this graph' % name)
        if update:
            for up_node in update:
                self.hashmax[up_node].append(name)
            #update graph with new edges
            #(HMGraph.create_node(int(len(self.matrix)+1),name,0))

    def remove_node(self,which = None):
        if which:
            del self.hashmax[which]
            for hash_list in self.hashmax.values():
                hash_list.remove(which)
        else:
            pass
            #if it's not set what to do?

    def insert_edge(self,node,target_edge):
        if not target_edge in self.hashmax[node]:
            self.hashmax[node].append(target_edge)
        else:
            self.double_round = True

    def print_hashMap(self,level = None):
        """
        Currently just pretty print.
        """
        pp = pprint.PrettyPrinter(indent=2)
        if level:
            pprint.pprint(self.hashmax,width=level)
        else:
            print('{')
            for key,val in self.hashmax.items():
                print('  \"%s\" : %s' % (key,val))
            print('}')

    def get_nodes(self):
        return sorted([nod for nod in self.hashmax.keys()])

    def get_edges(self):
        """
        for node in self.nodes:
            new_edges = [y for y in [x.keys() for x in self.matrix] if y
                    in self.nodes]
            if not self.edges.get(node) or self.edges[node] != new_edges:
                self.edges[node] = new_edges
        """
        # l = [1,2,3]
        #print(list(zip(['a' for b in l],[a for a in l])))
        #[zip(tup[0],[a for a in tup[1]]) for tup in [(node,edge) for node,edge
        # in self.hashmax.items()]]
        fin_edges = []
        for node,edges in self.hashmax.items():
            for edge in edges:
                fin_edges.append((node,edge))
        return fin_edges

    def insert_edges(self,data):
        """
        Depreciated!!
        search_que = [(data[x],data[x+1]) for x in range(len(data)-1)]
        operative = None
        for search_name in search_que:
            for element in self.matrix:
                if element['node_name'] == search_name[0]:
                    operative = element

            if operative:
                if search_name[1] not in operative.keys():

                    celkem zbytecne kdyz je to klic ale muzu sem narvat
                    dopravni prostredek napr misto repeat nazvu

                    print(self.nodes)
                    print("any",list(map(lambda x:x in
                        operative.keys(),self.nodes)))
                    if any(map(lambda x:x in operative.keys(),self.nodes)):
                        print([x for x in operative.keys() if x in self.nodes])
                        id_ = count([x for x in operative.keys() if x in self.nodes])
                    else:
                        id_ = 1

                    operative[search_name[1]] = HMGraph.create_node(
                            id_,search_name[1],1)
                else:
                    operative[search_name[1]]['counting'] += 1
            else:
                print('Error: No Node found')
    """

    #request for refactoing
    def find_most_used_node(self):
        """
        this is first task this may be putting into distribution.py
        l = []
        for x in self.matrix:
            count = 0
            if any(map(lambda y:y in x.keys(),self.nodes)):
                count = 1
                for a in [y for y in x.keys() if y in self.nodes]:
                    count += 1
            l.append((x['node_name'],count))

        return max(l, key=lambda x:x[1])
        """
        most_used = {}
        for key,val in self.hashmax.items():
            most_used[key] = 1 if val else 0
            most_used[key] += [True if key in val else False for val in
                    self.hashmax.values()].count(True)

        max_used = max(most_used, key = lambda k : most_used[k])
        return (max_used,most_used[max_used])

    #request for refactoing
    def has_double_edges(self):
        """
        this is second task, this also shout be inserted into distribution.py
        """
        for x in self.matrix:
            keys = [z for z in x.keys() if z in self.nodes]
            for a,b in x.items():
                if a in keys:
                    if b['counting'] > 1:
                        return True
        return False

    #request for refactoing
    def has_cycle(self):

        def dfs(graph, start):
            visited, stack = set(), [start]
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    stack.extend(graph[vertex] - visited)
            return visited

        graph = self.get_edges()
        for k,v in graph:
            if len(v) > 0:
                if k in dfs(graph,k):
                    return True
            else:
                pass

        return False

    def is_biparted(self):
        """
        is_biparted nejdrive si vytvori dict uzlu s None barvou a pak si
        vytvor
        """
        colors = {x: None for x in self.get_nodes()}
        #d = {key: value for (key, value) in iterable}

        graph = self.get_edges()
        visited, queue = set(), [start]
        colors[start] = "cervena"
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
                for x in graph[vertex] - visited:
                    if colors[x] == colors[vertex]:
                        return False
                    colors[x] = "zelena" if colors[vertex] == "cerverna" else "cerverna"

        return colors

    def find_clique(self):
        if not self.edges:
            self.get_edges()

        edges = {}
        for node,edges in self.edges.items():
            edges[node] = (edges,len(edges))
        while not all(leng[0] == leng for leng in [ed[1] for ed in edges.values()]):
            del_key = min([(ed,val) for ed,val in edges.times()],lambda x :
                x[1])[0]
            del edges[del_key]
            for node,edges in self.edges.items():
                new_edges = edges.remove(del_key)
                edges[node] = (new_edges,len(new_edges))

        return (fin_node for fin_node in edges.keys())

class LinkedGraph:
    """
    Implementace grafu pres ukazatele
    """

    pass

if __name__ == "__main__":
    test1 = HMGraph(['A','B','C'])
    test1.insert_edge('A','B')
    test1.insert_edge('B','C')
    test1.insert_edge('A','C')
    print("Nodes:",test1.get_nodes())
    print("Edges:",test1.get_edges())
    print("Double edges:",test1.double_round)
    test1.print_hashMap()
