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
                self.hashmax[spec_node.strip()] = []
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
        if target_edge in self.hashmax[node]:
            self.double_round = True
        else:
            self.hashmax[node].append(target_edge)

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

    def get_nodes(self,specific = None):
        nodes = sorted([nod for nod in self.hashmax.keys()])
        if not specific:
            return nodes
        else:
            return nodes[specific]

    def get_edges(self):
        """
        for node in self.nodes:
            new_edges = [y for y in [x.keys() for x in self.matrix] if y
                    in self.nodes]
            if not self.edges.get(node) or self.edges[node] != new_edges:
                self.edges[node] = new_edges
        """
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
        pass

    def find_most_used_node(self):
        """
        this is first task this may be putting into distribution.py
        """
        most_used = {key: 0 for key in self.get_nodes()}
        for key,val in self.hashmax.items():
            most_used[key] += len(val)
            most_used[key] += [True if key in val else False for val in
                    self.hashmax.values()].count(True)

        # pokud jsou stejne value tak vypsat vsechny
      #  if all[va for val in most_used.values()]
        max_used = max(most_used, key = lambda k : most_used[k])
        return (max_used,most_used[max_used])

    def has_cycle(self):

        def dfs(graph, node, color, found_cycle):
            if not found_cycle:
                color[node] = "gray"
                for vertex in graph[node]:
                    if color[vertex] == "gray":
                        found_cycle.append(True)
                        return
                    if color[vertex] == "white":
                        dfs(graph,vertex, color, found_cycle)
                color[node] = "black"
            else:
                return

        color = {node : "white" for node in self.get_nodes()}
        found_cycle = []
        graph = self.hashmax.copy()
        for node in self.get_nodes():
            if color[node] == "white":
                dfs(graph,node, color, found_cycle)
            if found_cycle:
                break
        return found_cycle

        """
        start = self.get_nodes()[0]
        visited, stack = [], [start]

        while stack:
            vertex = stack.pop()
            visited.append(vertex)
            for node in self.hashmax[vertex]:
                if node in stack:
                    return True
                if node not in visited:
                    stack.append(node)
        return False
        """

    def is_biparted(self):
        """
        is_biparted nejdrive si vytvori dict uzlu s None barvou a pak si
        vytvor
        d = {key: value for (key, value) in iterable}
        """
        colors = {x: None for x in self.get_nodes()}
        start = self.get_nodes()[0]
        visited, queue = set(), [start]
        colors[start] = "cervena"
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                for vert in self.hashmax[vertex]:
                        if vert not in visited:
                            queue.append(vert)
                for x in [node for node in self.get_nodes() if node not in
                        visited]:
                    if colors[x] == colors[vertex]:
                        return False
                    colors[x] = "zelena" if colors[vertex] == "cerverna" else "cerverna"

        return colors

    def find_clique(self):

        def contin(edges):
            counter = [count_edges[1] for count_edges in edges.values()]
            return all([counter[0] == leng for leng in counter])

        def body(edited_hash):
            counting_edges = {}
            for vertex, edit_edge in edited_hash.items():
                counting_edges[vertex] = (edit_edge[:],len(edit_edge))

            while not contin(counting_edges):
                del_key = min([(ed,val) for ed,val in
                    counting_edges.items()],key = lambda x : x[1][1])[0]
                #mazani vsech uzlu v klice
                del counting_edges[del_key]
                # oprava ostatnich poli
                for node, edge in counting_edges.items():
                    try:
                        edge[0].remove(del_key)
                        new_edge_list = edge[0]
                    except ValueError:
                        new_edge_list = edge[0]
                    except AttributeError:
                        new_edge_list = edge[0]
                    counting_edges[node] = (new_edge_list,len(new_edge_list))

            #vratim kliku,upraveny hash
            clique = []
            for cliq_node in counting_edges.keys():
                del edited_hash[cliq_node]
                for editing_key in edited_hash.keys():
                    try:
                        edited_hash[editing_key].remove(cliq_node)
                    except ValueError:
                        pass
                    except AttributeError:
                        pass
                clique.append(cliq_node)

            return (clique,edited_hash)

        cliques = []
        graph = self.hashmax.copy()
        while graph:
            (cli,graph) = body(graph)
            cliques.append(cli)
        return cliques

class LinkedGraph:
    """
    Implementace grafu pres ukazatele
    """

    pass

if __name__ == "__main__":
    test1 = HMGraph(['A','B','C','D','E'])
    test1.insert_edge('A','B')
    test1.insert_edge('B','A')
    test1.insert_edge('A','C')
    test1.insert_edge('C','A')
    test1.insert_edge('B','C')
    test1.insert_edge('C','B')
    test1.insert_edge('C','D')
    test1.insert_edge('D','C')
    test1.insert_edge('D','E')
    test1.insert_edge('E','D')
    print("Nodes:",test1.get_nodes())
    print("Edges:",test1.get_edges())
    test1.print_hashMap()
    print("Find most used:",test1.find_most_used_node())
    print("Double edges:",test1.double_round)
    start = test1.get_nodes()[0]
    print("Has cycle:","Yes" if test1.has_cycle() else "No")
    print("Is biparted:",test1.is_biparted())
    print("Main clique: ",test1.find_clique())
