from helper_functions import *


def one_way_connection(G):
    neighbours_tup = []
    for i in nodes:
        neighbours = getNeighbors(G, i)
        for j in neighbours:
            neighbours_tup.append((i, j))

    for i in neighbours_tup:
        j = (i[1], i[0])
        if j in neighbours_tup:
            neighbours_tup.remove(i)
            neighbours_tup.remove(j)
    
    return neighbours_tup


def nearest_airport(G, A):
    return getNearestNeighbor(G, A)

def not_more_than_one_intermediate(G, node):
    output = []
    for i in G.keys():
        for j in G[i]:
            if j[0] == node:
                output.append(i)
                break
            else:
                for k in G[j[0]]:
                        if k[0] == node:
                            output.append(i)
                            break
    output.remove(node)                       
    return output
    
                    
    
G = {}
nodes = ["Austin", "Dallas", "Washington", "Atlanta", "Houston", "Chicago", "Denver"]
edges = [
         ("Austin", "Dallas", 200), ("Austin", "Houston", 160), 
         ("Dallas", "Austin", 200), ("Dallas", "Denver", 780), ("Dallas", "Chicago", 900),
         ("Washington", "Dallas", 1300), ("Washington", "Atlanta", 600), 
         ("Atlanta", "Washington", 600), ("Atlanta", "Houston", 800),
         ("Houston", "Atlanta", 800), 
         ("Chicago", "Denver", 1000),
         ("Denver", "Atlanta", 1400), ("Denver", "Chicago", 1000), 
         ]

addNodes(G, nodes)
addEdges(G, edges, directed = True)
displayGraph(G)

removeNode(G, "Washington")
G["Atlanta"].append(("Dallas", 1700))
displayGraph(G)


    





'''
EXPECTED OUTPUT:

GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}

ONE WAY CONNECTION
[('Dallas', 'Denver'), ('Dallas', 'Chicago'), ('Austin', 'Houston'), ('Washington', 'Dallas'), ('Denver', 'Atlanta')]

NEAREST AIRPORT
Dallas : Austin
Austin : Houston
Washington : Atlanta
Denver : Chicago
Atlanta : Washington
Chicago : Denver
Houston : Atlanta

CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT
Dallas : ['Austin', 'Washington', 'Atlanta']

REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900), ('Atlanta', 1700)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Houston', 800), ('Dallas', 1700)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
'''