from Question2 import *
 
def stutter(A, n):
    new_q = Initialize(NumberOfElements(A)*n)
    while is_empty(A) == False:
        new_n = deQueue(A)
        for i in range(n):
            enQueue(new_q, new_n)
    return new_q

if __name__ == "__main__":
    print(stutter([1, 2, 3], 2))
    # Should print "[1, 1, 2, 2, 3, 3]"

    print(stutter(['a', 'b', 'c'], 3))
    # Should print "['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']"