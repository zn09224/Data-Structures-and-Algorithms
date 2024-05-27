from Question1 import *
from Question2 import *

def put(hashtable,key, data,size):
    
    hashvalue = hash_function(key, size)
    
    if hashtable[0][hashvalue] == None:
        hashtable[0][hashvalue] = key
        hashtable[1][hashvalue] = data
    else:
        count = 1
        new_hash = collision_resolver(key, size, count)

        while hashtable[0][new_hash] != None and hashtable[0][new_hash] != key and count != size:
            count += 1
            new_hash = collision_resolver(key, size, count)
        
        if hashtable[0][new_hash] == None:
            
            hashtable[0][new_hash] = key
            hashtable[1][new_hash] = data
        
        else:
            
            if hashtable[0][new_hash] == key:
                
                hashtable[1][new_hash] = data
    
        
def get(hashtable,key,size):
    
    start = hash_function(key, size)
    pos = start
    count = 1
    
    while hashtable[0][pos] != None:
        
        if key == hashtable[0][pos] and hashtable[0][pos] != '#':
            return hashtable[1][pos]
        
        else:
            
            pos = collision_resolver(key, size, count)
            count += 1
            if pos == start:
                break
    
    return None
            
            
        

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    print(get(H,5,10)) # Should print 3