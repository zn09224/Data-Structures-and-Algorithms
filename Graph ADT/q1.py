from helper_functions import *


'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}

LIST OF NODES
[1, 2, 3, 4, 5]

LIST OF EDGES
[(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]

NEIGHBOURS FOR EACH NODE IN A GRAPH
1 : [2, 5]
2 : [1, 3, 4, 5]
3 : [2, 4]
4 : [2, 3, 5]
5 : [1, 2, 4]
'''

G = {}
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]
 
addNodes(G, nodes)
addEdges(G, edges, directed = False)
displayGraph(G)

print(listOfNodes(G))
print(listOfEdges(G, directed=False))

for i in nodes:
    print(i, ":", getNeighbors(G, i))

