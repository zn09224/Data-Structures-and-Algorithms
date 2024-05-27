from Helper_Functions import *

def dfs(G,s):
    visited = []
    stack = []
    stack.append(s)
    visited.append(s)
    while len(stack) > 0:
        a = stack.pop()
        if a not in visited:
            visited.append(a)
        for i in G[a]:
            if i[0] not in visited:
                stack.append(i[0])
    return visited


# # Testing 
G = {0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}
print(dfs(G,1 ))
# # Should print [0, 2, 4, 5, 1, 3]