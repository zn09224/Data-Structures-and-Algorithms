from HelperFunctions import *

def Question1():
  
  # Question 1a
  keys = [68, 88, 61, 89, 94, 50, 4, 76, 66, 82]
  bst = {}
  for i in keys:
    insert(bst, i)  
  print(bst)  

  # Question 1b
  print(exist(bst, 50))

  # Question 1c
  print(exist(bst, 49))
  
  # Question 1d
  print(minimum(bst, 68))

  # Question 1e
  print(minimum(bst, 88))

  # Question 1f
  print(maximum(bst, 68))
  
  # Question 1g
  print(maximum(bst, 61))

  # Question 1h
  result = []
  print(inorder_traversal(bst, result))

  # Question 1i
  result = []
  print(preorder_traversal(bst, result))

  # Question 1j
  result = []
  print(postorder_traversal(bst, result))

  # Question 1k
  print(successor(bst, 76, successor_node = None))
  

## Testing
Question1()

## Expected Outputs
## 1a
# {'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}

## 1b
# True 

## 1c
# False 

## 1d
# {'value': 4, 'left': {}, 'right': {}}

## 1e
# {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}

## 1f
# {'value': 94, 'left': {}, 'right': {}}

## 1g
# {'value': 66, 'left': {}, 'right': {}}

## 1h
# [4, 50, 61, 66, 68, 76, 82, 88, 89, 94]

## 1i
# [68, 61, 50, 4, 66, 88, 76, 82, 89, 94]

## 1j
# [4, 50, 66, 61, 82, 76, 94, 89, 88, 68]

## 1k
# 82