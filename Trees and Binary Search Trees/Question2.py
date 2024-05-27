from HelperFunctions import *

def Question2():
    given_list = ["begin", "do", "else", "end", "if", "then", "while"]
    bst = {}
    for word in given_list:
        insert(bst, word)
        
    print(bst)
        

## Testing
Question2()

## Expected Output
# {'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}