from HelperFunctions import *
from Question2 import GetShortestPath

def GetShortestDistanceBetweenCities(source,destination):
    
    with open ('connections.csv') as f :
        lines = f.readlines()
        
    input = []
    for line in lines :
        line = line.strip() 
        tokens = line.split(",") 
        input.append(tokens) 

    nodes = []
    for i in input[0][1:]:
        nodes.append(i)
    
    edges = []
    for i in input[1:]:
        for j in range(len(nodes)):
            if i[j + 1] != '-1':
                edges.append((i[0], nodes[j], int(i[j + 1])))
    
    G = {}
    
    AddNodes(G, nodes)
    AddEdges(G, edges)    
    
    return GetShortestPath(G, source, destination)
    
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))
    