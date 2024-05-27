# Helper Function #1
def insert(bst, key):
    if bst == {}:
        bst["value"] = key
        bst["left"] = {}
        bst["right"] = {}
    if key > bst["value"]:
        insert(bst["right"], key)
    elif key < bst["value"]:
        insert(bst["left"], key)

# Helper Function #2
def exist(bst, key):
    if bst == {}:
        return False
    if bst["value"] == key:
        return True
    if key < bst["value"]:
        return exist(bst["left"], key)
    elif key > bst["value"]:
        return exist(bst["right"], key)
    
# Helper Function #3
def minimum(bst, starting_node):
    temp = goto(bst, starting_node)
    return min(temp)

# Helper Function #4
def maximum(bst,starting_node):
    temp = goto(bst, starting_node)
    return max(temp)
    

# Helper Function #5
def inorder_traversal(bst, res):
    if bst == {}:
        return res
    else:
        inorder_traversal(bst["left"], res)
        res.append(bst["value"])
        inorder_traversal(bst["right"], res)
        return res

# Helper Function #6
def preorder_traversal(bst, res):
    if bst == {}:
        return res
    else:
        res.append(bst["value"])
        preorder_traversal(bst["left"], res)
        preorder_traversal(bst["right"], res)
        return res

# Helper Function #7
def postorder_traversal(bst, res):
    if bst == {}:
        return res
    else:
        postorder_traversal(bst["left"], res)
        postorder_traversal(bst["right"], res)
        res.append(bst["value"])
        return res
    
# Helper Function #8
def successor(bst, key, successor_node=None):
    temp = goto(bst, key)
    if temp["right"] == {}:
        return successor_help(bst, key, successor_node = key)
    elif temp["right"]["left"] == {}:
        return temp["right"]["value"]
    else:
        return min_2(temp["right"])

# Additional Functions:
def goto(bst, starting_node):
    if bst == {}:
        return "DNE"
    if bst["value"] == starting_node:
        return bst
    if starting_node < bst["value"]:
        return goto(bst["left"], starting_node)
    elif starting_node > bst["value"]:
        return goto(bst["right"], starting_node)

def min(bst):
    if bst["left"] == {}:
        return bst
    else:
        return min(bst["left"])
    
def max(bst):
    if bst["right"] == {}:
        return bst
    else:
        return max(bst["right"])
    
def min_2(bst):
    if bst["left"] == {}:
        return bst["value"]
    else:
        return min_2(bst["left"])

def successor_help(bst, key, successor_node):
    if bst["value"] == key:
        if successor_node == key:
            return None
        else:
            return successor_node
    if key < bst["value"]:
        return successor_help(bst["left"], key, successor_node = bst["value"])
    elif key > bst["value"]:
        return successor_help(bst["right"], key, successor_node)
      
    