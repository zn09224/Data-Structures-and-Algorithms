from HelperFunctions import *
from Question2 import GetShortestPath
def GetShortestPathGrid(grid,source,destination):
    graph = {}
    nodes = []
    edges = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            nodes.append((i, j))
            if grid[i][j] == 1:
                for l in range(i-1, i + 2):
                    if l < 0 or l >= len(grid):
                        continue
                    for k in range(j - 1, j + 2):
                        if k < 0 or k >= len(grid[i]) or (l != i and k != j):
                            continue
                        else:
                            if grid[l][k] != -1 and (l != i or j != k) and ((i, j), (l, k), 1) not in edges:
                                edges.append(((i, j), (l, k), 1))
    AddNodes(graph, nodes)
    AddEdges(graph, edges, True)
    
    print(graph)
    return GetShortestPath(graph, source, destination)

if __name__ == "__main__":
    grid = [[1, 1, 1, -1, 1, 1], [1, -1, 1, 1, 1, 1], [-1, 1, 1, -1, 1, 1], [1, 1, -1, 1, 1, 1], [1, -1, 1, 1, 1, 1], [1, 1, -1, 1, 1, 1]]
    source = (0, 0)
    destination = (5,5)
    print(GetShortestPathGrid(grid, source, destination))


        