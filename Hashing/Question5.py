from Question4 import *

def main(to_put,to_delete,to_get,size): # returns tuple(list,hash table)
    
    hashtable = create_hashtable(size)
    
    for i in to_put:
        put(hashtable, i[0], i[1], size)
    
    for i in to_delete:
        delete(hashtable, i, size)
    
    output = []
    for i in to_get:
        output.append(get(hashtable, i, size))
    
    return ((output, hashtable))
        

if __name__ == "__main__":
    size = 5
    to_put = [(1 ,2) ,(" key "," value")]
    to_delete = [1]
    to_get = [" key "]
    print(main (to_put , to_delete , to_get , size))
    # Shoud print ([' value '], ([None, '#', None, ' key ', None], [None, '#', None, ' value ', None]))
    
    




def merge_sort(S):
    n = len(S)
    if n <= 1:
        return S
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

def merge(S1, S2, S):
    i = j = 0
    while (i + j < len(S)):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1