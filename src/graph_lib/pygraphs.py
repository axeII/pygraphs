""" Pygraphs

Graph library, this file should be splitted when goes bigger.
"""

__author__ = 'Ales Lerch'

import os
import sys
import math
import pprint
import random
import collections

"""
graph = { "a" : [("c",4)],
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

    def __init__(self,setup_nodes = [], edges_with_val = False):
        """
        Maybe different library for for hashmax if to include order key inputs if
        needed in this data structure
        data_dict = collections.OrderedDict(sorted(data_dict.items()))
        """
        self.hashmax = {}
        self.hashmax = collections.OrderedDict()
        self.double_round = False
        self.edges_value = edges_with_val
        if setup_nodes and isinstance(setup_nodes,list):
            """
            In case to use indexes as int use range(len(setup_nodes))
            else let it as key name it's python
            """
            for spec_node in setup_nodes:
                self.hashmax[spec_node.strip()] = []

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
                """
                update graph with new edges
                """

    def remove_node(self,which = None):
        """
        there should be somthing done with else statement, what to do if which
        is set?
        """
        if which:
            del self.hashmax[which]
            for hash_list in self.hashmax.values():
                hash_list.remove(which)
        else:
            pass

    def insert_edge(self,node,target_edge,edge_val = None):
        """
        current dilema on graph structure - should be same architecture
        with value as zeros like g : ('n',0) or have two architerues
        """
        if not self.edges_value:
            if target_edge in self.hashmax[node]:
                self.double_round = True
            else:
                self.hashmax[node].append(target_edge)

        elif self.edges_value and edge_val:
            if target_edge in map(lambda x:x[0], self.hashmax[node]):
                self.double_round = True
            else:
                self.hashmax[node].append((target_edge,edge_val))

    def print_hashMap(self, sorted_ = False, level = None):
        """
        Currently just pretty print.
        """
        pp = pprint.PrettyPrinter(indent=2)
        if level:
            pprint.pprint(self.hashmax,width=level)
        else:
            print('{')
            if sorted_:
                for key,val in sorted(self.hashmax.items(), key=lambda x:x[0]):
                    print('  \"%s\" : %s' % (key,sorted(val,key=lambda x:x[0])))
            else:
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
        fin_edges = []
        for node,edges in self.hashmax.items():
            for edge in edges:
                fin_edges.append((node,edge))
        return fin_edges

    def find_most_used_node(self):
        """
        this is first task this may be putting into distribution.py
        if all values are same then output all of them
        if all[va for val in most_used.values()]
        """
        most_used = {key: 0 for key in self.get_nodes()}
        for key,val in self.hashmax.items():
            most_used[key] += len(val)
            most_used[key] += [True if key in val else False for val in
                    self.hashmax.values()].count(True)

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
        this works only on undirected graph
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

    def is_a_tree(self):
        """
        inicialization may look weird but it's all because new checker
        anyway bfs for serach nodes if not foudn same node continue 
        else end, if foudn nodes compare to inicial node if same 
        return true
        """
        visited = stack = []
        if self.get_nodes():
            stack = [self.get_nodes()[0]]

        while stack:
            vertex = stack.pop(0)
            visited.append(vertex)
            for next_ in self.hashmax[vertex]:
                if not next_ in visited:
                    stack.append(next_)
                else:
                    return False

        return True if visited == self.get_nodes() else False

    def is_biparted(self):
        """
        is_biparted fistly create dict of nodes with None color and then create
        other... not woking - fix it!
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

    def find_graph_skeleton(self):
        key = 0
        min_ = math.inf
        key_edge = ()
        skeleton = []
        visited = set()
        copy_graph = self.hashmax.copy()

        if self.edges_value and self.hashmax:
            while sorted(list(visited)) != self.get_nodes():
                """
                min_edge = min([(x,y) for x,y in copy_graph.items()],key = lambda x: x[1])
                min_edge_reverse = (min_edge[1][0],min_edge[0])
                map(lambda x: visited.add(x),[min_edge[0],min_edge[1][0]])
                nedalo by se toto taky dat jenom na jeden radek
                """
                for x,y in copy_graph.items():
                    if y:
                        val = min(y,key = lambda b : b[1])[1]
                        if val < min_:
                            min_ = val
                            key_edge = min(y,key = lambda b : b[1])
                            key = x
                if copy_graph[key]:
                    copy_graph[key].remove(key_edge)
                if copy_graph[key_edge[0]]:
                    copy_graph[key_edge[0]].remove((key,key_edge[1]))
                skeleton.append((key,key_edge))
                visited.add(key)
                visited.add(key_edge[0])
                min_ = math.inf

        return skeleton

    def find_articulation(self):
        answer = {}
        for node in self.get_nodes():
            #print(node)
            copy_graph = {}
            for node_, edge in self.hashmax.items():
                copy_graph[node_] = edge[:]
            del copy_graph[node]
            for edge in copy_graph.values():
                try:
                    edge.remove(node)
                except ValueError:
                    pass
            visited = []
            stack = [random.choice(list(copy_graph.keys()))]
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.append(vertex)
                for next_ in copy_graph[vertex]:
                    if next_ not in visited:
                        stack.append(next_)

            edited = self.get_nodes()
            edited.remove(node)
            answer[node] = True if sorted(visited) == edited else False
        return answer

    def find_bridge(self,articulations):
        if articulations:
            bridges = {}
            for key, val in articulations.items():
                respond = {}
                if not val:
                    for next_node in self.hashmax[key]:
                        copy_graph = {}
                        for node_, edge in self.hashmax.items():
                            copy_graph[node_] = edge[:]
                        copy_graph[key].remove(next_node)
                        copy_graph[next_node].remove(key)
                        """
                        go through whole graph and find out if there is another
                        complete
                        """
                        visited = []
                        stack = [random.choice(list(copy_graph.keys()))]
                        while stack:
                            vertex = stack.pop()
                            if vertex not in visited:
                                visited.append(vertex)
                            for next_ in copy_graph[vertex]:
                                if next_ not in visited:
                                    stack.append(next_)

                        respond[next_node] = True if sorted(visited) == self.get_nodes() else False
                    bridges[key] = respond
            return bridges
        else:
            return "Error: No input articulations"

    def djikstra(self,first,number = 0):
        if self.edges_value and first:
            djisktra = {x: [None,math.inf] for x in self.get_nodes() if x != first}
            djisktra[first] = [None,0]
            stack, visited = [(first,0)], []
            while number <= len(self.get_nodes()) and stack:
                number += 1
                vertex = stack.pop(0)
                visited.append(vertex[0])
                for edge in self.hashmax[vertex[0]]:
                    calculated = djisktra[vertex[0]][1] + edge[1]
                    if calculated < djisktra[edge[0]][1]:
                        djisktra[edge[0]] = [vertex,calculated]
                for next_ in self.hashmax[vertex[0]]:
                    if not next_[0] in visited:
                        stack.append(next_)
            return djisktra
        else:
            return "Error something went wrong"

    """
    this methond is commented due to killing cpu
    1)Vytvorim graf na cyklu,2)Odecist z radku min, 3)Kde je nula tam je phi,4) Najit
    nejvetsi phi,5) Tvrit hranu do grafu,6) Smazat hranu z matice, 7) Vytvorit opacne
    inf, 8) konec self.max.nodes == new graf nodes
    """
    def travelling_salesman(self):
        salesman = {}
        travel = HMGraph(self.get_nodes())
        for key in sorted(self.hashmax.keys()):
            salesman[key] = sorted(self.hashmax[key][:], key = lambda x : x[0])

        while len(salesman.keys()) > 1:#not all(travel.hashmax.values()):some node is empty of graph
            for row in sorted(salesman.keys()):
                min_ = min(salesman[row],key = lambda x: x[1])
                coa = [col for col in salesman[row] if col[1] != math.inf]
                if len([col for col in salesman[row] if col[1] != math.inf]) >= 2:
                    new_row = []
                    for column in salesman[row]:
                        new_row.append((column[0],column[1] - min_[1]))
                    salesman[row] = new_row
            """
            jeste bych mel dodelat vertikalni nuly vsude
            """
            zeros = {}
            for key, row in salesman.items():
                for column in row:
                    if column[1] == 0:
                        min_row = min([r for r in row if r != column], key = lambda x: x[1])
                        min_column = [[(r[0],r[1]) for r in row_ if r[0] ==
                            column[0] and row != row_] for row_ in salesman.values()]
                        min_column = min([min_[0] for min_ in min_column if min_],key=lambda x:x[1])
                        zeros[(key,column[0])] = min_row[1] + min_column[1]

            if zeros:
                sigma = max(sorted(zeros.items(),key=lambda x:x[0]),key=lambda x: x[1])
                travel.insert_edge(sigma[0][0],sigma[0][1])
                del salesman[sigma[0][0]]
                for key, val in salesman.items():
                    salesman[key] = [(v[0],float("inf")) if key == sigma[0][1] and v[0] ==
                            sigma[0][0] else v for v in val if v[0] != sigma[0][1]]
        return travel

    def floyd_warshall(self):
        floyd = {}
        theta = len(self.get_nodes())
        for key, val in sorted(self.hashmax.items(),key=lambda x: x[1]):
            floyd[key] = sorted(val[:], key = lambda x : x[0])
            floyd[key].append((key,0))

        matrix = []
        for key, val in sorted(floyd.items(), key=lambda x: x[0]):
            matrix.append([s[1] for s in sorted(val, key = lambda x : x[0])])

        for k in range(0, theta):
            for i in range(0, theta):
                for j in range(0, theta):
                    matrix[i][j] = max(matrix[i][j], matrix[i][k] + matrix[k][j])

        for k in range(0, theta):
            for i in range(0, theta):
                for j in range(0, theta):
                    if (matrix[i][k] + matrix[k][j] < matrix[i][j]):
                        matrix[i][j] = float("-inf")

    def cpm_long(self,first_node):
        cpm_nodes = {x: (None,0) for x in self.get_nodes()}

        for key, val in sorted(self.hashmax.items(),key=lambda x: x[0]):
            for v in val:
                cpm_nodes[v[0]] = max(cpm_nodes[v[0]],
                        (key,v[1]+cpm_nodes[key][1]),key=lambda x:x[1])

        return sorted(cpm_nodes.items(),key=lambda x:x[0])

    def find_clique(self):

        def contin(edges):
            counter = [count_edges[1] for count_edges in edges.values()]
            return all([counter[0] == leng for leng in counter])

        def body(edited_hash):
            """
            body delet all nodes that are in clique, and others field then
            return clique and updated hash table-dict
            """
            counting_edges = {}
            for vertex, edit_edge in edited_hash.items():
                counting_edges[vertex] = (edit_edge[:],len(edit_edge))

            while not contin(counting_edges):
                del_key = min([(ed,val) for ed,val in
                    counting_edges.items()],key = lambda x : x[1][1])[0]
                del counting_edges[del_key]
                for node, edge in counting_edges.items():
                    try:
                        edge[0].remove(del_key)
                        new_edge_list = edge[0]
                    except ValueError:
                        new_edge_list = edge[0]
                    except AttributeError:
                        new_edge_list = edge[0]
                    counting_edges[node] = (new_edge_list,len(new_edge_list))

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

if __name__ == "__main__":
    test1 = HMGraph(['A','B','C','D'],True)
    test1.insert_edge('A','B',1)
    test1.insert_edge('A','C',3)
    test1.insert_edge('B','A',1)
    test1.insert_edge('B','C',2)
    test1.insert_edge('C','B',2)
    test1.insert_edge('C','A',3)
    test1.insert_edge('C','D',5)
    test1.insert_edge('D','C',5)
    print("Nodes:",test1.get_nodes())
    print("Edges:",test1.get_edges())
    test1.print_hashMap()
    #test1.travelling_salesman()
