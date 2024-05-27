from Question3 import *

def delete(hashtable, key, size):
    
    hash_value = hash_function(key, size)
    new_hash = hash_value
    
    if hashtable[0][hash_value] != key:
        
        count = 1
        while hashtable[0][new_hash] != key and count != size:
            
            new_hash  = collision_resolver(key, size, count)
            count += 1
        
        hashtable[0][new_hash] = '#'
        hashtable[1][new_hash] = '#'
    
    else:
        hashtable[0][hash_value] = '#'
        hashtable[1][hash_value] = '#'
    
                
            
        
        

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    delete(H,5,10)
    print(H)
    # Should print ([None, None, None, None, None, '#', None, None, None, None], [None, None, None, None, None, '#', None, None, None, None])