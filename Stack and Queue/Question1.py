from listADT import *

def push(lst, item):
    for i in range(len(lst)):
        if lst[i] == None:
            lst[i] = item
            break

def pop(lst):
    if lst[0] == None:
        return "Error"
    if lst[len(lst)-1] != None:
        return lst[len(lst)-1]
    for i in range(len(lst)):
        if lst[i] == None:
            element = lst[i-1]
            lst[i-1] = None
            return element

def top(lst):
    if lst[0] == None:
        return "Error"
    if lst[len(lst)-1] != None:
        return lst[len(lst)-1]
    for i in range(len(lst)):
        if lst[i] == None:
            element = lst[i-1]
            return element

def is_empty(lst):
    for i in range(len(lst)):
        if lst[i] != None:
            return False
    return True

if __name__ == "__main__":
    stack = Initialize(5)
    # Initialize a stack of size 5

    print(is_empty(stack))
    # Should print "True"

    push(stack, 1)
    print(stack)
    # Should print "[1, None, None, None, None]"

    push(stack, 2)
    print(stack)
    # Stack should print "[1, 2, None, None, None]"

    print(pop(stack))
    # Should remove the intger 2 from stack and print "2"

    print(top(stack))
    # Should ONLY print "1" which is at the top of the stack

    print(stack)
    # Should print the entire stack which is "[1, None, None, None, None]"