def addNodes(G, nodes):
    for i in nodes:
        G[i] = []

def addEdges(G, edges, directed=False):
    if directed == False:
        for i in edges:
            if i not in G[i[0]]:
                G[i[0]].append((i[1], i[2]))
            if i not in G[i[1]]:
                G[i[1]].append((i[0], i[2]))
    else:
        for i in edges:
            if i not in G[i[0]]:
                G[i[0]].append((i[1], i[2]))
        
def displayGraph(G):
    print(G)

def listOfNodes(G):
    return list(G.keys())

def listOfEdges(G, directed=False):
    output = []
    if directed == False:
        nodes = list(G.keys())
        for i in nodes:
            for j in G[i]:
                to_append = (i, j[0], j[1])
                not_to_append = (j[0], i, j[1])
                if to_append not in output and not_to_append not in output:
                    output.append(to_append)
    else:
        nodes = list(G.keys())
        for i in nodes:
            for j in G[i]:
                to_append = (i, j[0], j[1])
                if to_append not in output:
                    output.append(to_append)
    
    return output
        
            

def getNeighbors(G, nodes):
    neighbours = []
    for i in G[nodes]:
        neighbours.append(i[0])
    return neighbours

def removeNode(G, node):
    for i, j in G.items():
        for k in j:
            if k[0] == node:
                j.remove(k)
    del G[node]
                

def removeNodes(G, nodes):
    for i in nodes:
        removeNode(G, i)

def getNearestNeighbor(G, node):
    min = G[node][0][1]
    for i in G[node]:
        if i[1] <= min:
            min = i[1]
            
    for i in G[node]:
        if i[1] == min:
            return i[0]