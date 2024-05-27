from HelperFunctions import *
from Question1 import *
def GetShortestPath(graph, source, destination):
    print(destination)
    output = []
    queue = []
    dist = {}
    prev = {}
    for v in graph.keys():
        prev[v] = None
        if v == source:
            dist[v] = 0
            EnQueue(queue, v, 0)
        else:
            dist[v] = float('inf')
            EnQueue(queue, v, float("inf"))
    while not IsEmpty(queue):
        v = DeQueue(queue)
        neighbours = GetNeighbors(graph, v)
        for i in neighbours:
            if dist[v] + i[1] < dist[i[0]]:
                dist[i[0]] = i[1] + dist[v]
                EnQueue(queue, i[0], dist[i[0]])
                prev[i[0]] = v
   
    dis = 0
    d = destination
    print(dist, prev)
    while d != source:
        for i in graph[d]:
            if i[0] == prev[d]:
                dis = i[1]
        output.append((prev[d], d, dis))
        d = prev[d]
        if d == None:
            break

    
    output = output[::-1]
    if len(output) == 0:
        output = -1
    return output
                  

if __name__ == "__main__":
    graph = {'A': [('D', 2), ('E', 6), ('B', 7)], 'B': [('C', 3), ('A', 7)], 'C': [('B', 3), ('D', 2), ('G', 2)], 'D': [('A', 2), ('C', 2), ('F', 8)], 'E': [('A', 6), ('F', 9)], 'F': [('D', 8), ('E', 9), ('G', 4)], 'G': [('C', 2), ('F', 4)]}
    print(GetShortestPath(graph, 'A', 'G'))
    
    



