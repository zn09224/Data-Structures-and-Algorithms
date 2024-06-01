import ast

def reverse_karatsuba(data) -> tuple:
    
    i = 0
    while not is_leaf(data):        # Run until only leaf nodes are left
        i += 1
        if isinstance(data[i % len(data)], list):
            data[i % len(data)] = reverse_karatsuba(data[i % len(data)])    # Call reverse karatsuba recursively on nested lists
    
    # Merge the first and last tuple and return
    return (int(str(data[2][0]) + str(data[0][0])), int(str(data[2][1]) + str(data[0][1])))
    
    
def is_leaf(branch):        # Return True if the list only contains leaves i.e tuples
    
    count = 0       # Variable to store number of tuples in the branch
    for i in branch:
        if isinstance(i, tuple):
            count += 1
    if count == 3:
        return True
    else:
        return False
        
        

def main(filename) -> list[tuple[int, int]]:
    
    with open (filename) as f:
        lines = f.readlines ()
    input = []
    for line in lines:
        line = line.strip() 
        tokens = line.split("\n") 
        input.append(tokens)
    
    trees = []      # Initializing the list containing given lists as nested lists
    
    for tree in input[1:]:      # Iterating over each line of the given input skipping the first line
        tree = tree[0]
        tree = ast.literal_eval(tree)       # Converting the nested lists from string form to actual python lists form
        trees.append(tree)
    
    final = []      # Output List
    for i in trees:
        final.append(reverse_karatsuba(i))      # Calling reverse karatsuba for each given list
    
    return final       
        
main("input_decrypt.txt")