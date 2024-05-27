from Helper_Functions import *

def nodes_of_level(G, level):
    nodes = list(G.keys())
    root = nodes[0]
    visited = []
    queue = [None for _ in range(1000)]
    enQueue(queue, (root, 0))  
    visited.append(root)  
    out = []
    while not is_empty(queue):
        node, curr_level = deQueue(queue) 
        if curr_level == level:
            out.append(node)
        elif curr_level > level:
            break 
        for i in G[node]:
            if i[0] not in visited:
                enQueue(queue, (i[0], curr_level + 1))  
                visited.append(i[0])
    return sorted(out)



# # Testing
#G = {'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}

#print(nodes_of_level(G, 3))
# # Should print [7]

# print(nodes_of_level(G, 1))
# # Should print [1, 2]