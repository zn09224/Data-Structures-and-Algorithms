from Helper_Functions import *

def check_cycles(G,lst):
    j = 0
    s = lst[j]
    visited = []
    stack = [None for i in range(1000)]
    push(stack, s)
    visited.append(s)
    while not is_empty(stack):
        a = pop(stack)
        j = j + 1
        if a not in visited:
            visited.append(a)
        for i in G[a]:
            if j != len(lst) and i[0] not in visited and i[0] == lst[j]:
                push(stack, i[0])
            elif j == len(lst) and i[0] == lst[0]:
                return True
    return False



# # Testing
# G = {'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
# print(check_cycles(G, ['Dallas','Denver','Atlanta','Washington']))
# # Should print True