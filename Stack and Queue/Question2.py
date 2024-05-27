from listADT import *

def enQueue(lst, item):
    for i in range(len(lst)):
        if lst[i] == None:
            lst[i] = item
            break

def deQueue(lst):
    number = 0
    for element in lst:
        if element is None:
            break
        else:
            number += 1
    s = lst[0]
    lst[0] = None
    for i in range(1, len(lst)):
        lst[i-1] = lst[i]
        lst[i] = None
    return s

def front(lst):
    return lst[0]

def is_empty(lst):
    if IsEmpty(lst) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    Queue = Initialize(5)
    # Initialize a queue of size 5

    print(is_empty(Queue))
    # Should print "True" as Queue is empty

    enQueue(Queue, 5)
    print(Queue)
    # Should print "[5, None, None, None, None]"

    print(is_empty(Queue))
    # Should print "False" as Queue is non-empty

    enQueue(Queue, 7)
    print(Queue)
    # Should print "[5, 7, None, None, None]"

    print(front(Queue))
    # Should print "5"

    print(deQueue(Queue))
    # Should print "5"

    print(Queue)
    # Should print "[7, None, None, None, None]"

    print(front(Queue))
    # Should print "7"

    deQueue(Queue)
    print(Queue)
    # Should print "[None, None, None, None, None]"
