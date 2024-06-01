def create_hashtable(size):
    return ([None for _ in range(size)], [None for _ in range(size)])

def resize_hashtable(hashtable, size, increase): #return hashtable,size
    
    # Increase the size if required:
    if increase == True:
       new_size = next_prime(size * 2)
    
    # Decrease the size if required:
    else:
        new_size = next_prime(size // 2)
        
        # Condition to check if the size is not getting less than 7:
        if new_size < 7:    
            new_size = 7          
    
    new_hashtable = ([None for _ in range(new_size)], [None for _ in range(new_size)])
    
    keys, values = hashtable
    
    for i in range(len(keys)):
        if keys[i] != None:
            put(new_hashtable, keys[i], values[i], new_size)
        
    return new_hashtable, new_size

    
def hash_function(key, size): #returns integer (Address)
    
    sum = 0
    
    for character in key:
        sum += ord(character)
    
    # Right shift 4 bits:
    shifted = sum >> 4
    
    return abs(shifted % size)

def collision_resolver(key, oldAddress, size): #returns integer (Address)
    
    sum = 0
    
    for character in key:
        sum += ord(character)
    
    offset = sum // size
    
    return ((offset + oldAddress) % size)
        

def put(hashtable,key, data,size): #return hashtable,size
    
    hashvalue = hash_function(key, size)
    
    # If no collision occurs:
    if hashtable[0][hashvalue] == None or hashtable[0][hashvalue] == '#':   
        hashtable[0][hashvalue] = key
        hashtable[1][hashvalue] = data
    
    # In case of collision:
    else:
        
        count = 1       # Variable to keep check if the hashtable is not full
        
        new_hashvalue = collision_resolver(key, hashvalue, size)

        while hashtable[0][new_hashvalue] != None and hashtable[0][new_hashvalue] != '#' and hashtable[0][new_hashvalue] != key and count != size:
            
            count += 1
            new_hashvalue = collision_resolver(key, new_hashvalue, size)
        
        # If empty space found:
        if hashtable[0][new_hashvalue] == None or hashtable[0][new_hashvalue] == '#': 
            hashtable[0][new_hashvalue] = key
            hashtable[1][new_hashvalue] = data
        
        # If key already exists in the hashtable:
        elif hashtable[0][new_hashvalue] == key:
            hashtable[1][new_hashvalue] = data
    
    # Resizing if required:
    if loadFactor(hashtable, size) > 75:
        hashtable, size = resize_hashtable(hashtable, size, True)
        
    elif loadFactor(hashtable, size) < 30 and loadFactor(hashtable, size) > 0:
        if size != 7:       # No need to downsize if size is 7
            hashtable, size = resize_hashtable(hashtable, size, False)
        
    return hashtable, size

    
def loadFactor(hashtable, size): # Returns float load_factor as percentage
    
    keys, values = hashtable
    
    hashtable_population = 0
    
    # Calculating the number of elements in the hashtable:
    for i in keys:
        if i != None and i != '#':
            hashtable_population += 1
    
    load_factor = (hashtable_population / size) * 100

    return load_factor
            

def Update(hashtable, key, columnName, data, size, collision_path, opNumber): # returns Nothing, prints 'record Updated'
    
    hashvalue = hash_function(key, size)
    
    # If no collision occurs:
    if hashtable[0][hashvalue] == key:
        collision_path[opNumber].append(hashvalue)
        hashtable[1][hashvalue][columnName] = data
    
    # In case of collision:
    else:
        collision_path[opNumber].append(hashvalue)
        
        count = 1       # Variable to keep check if the whole hashtable is iterated / checked
        
        new_hashvalue = collision_resolver(key, hashvalue, size)
        
        while hashtable[0][new_hashvalue] != key and count != size:
            count += 1
            new_hashvalue = collision_resolver(key, new_hashvalue, size)
            collision_path[opNumber].append(new_hashvalue)
        
        # If the required key is found:
        if hashtable[0][new_hashvalue] == key:
            collision_path[opNumber].append(new_hashvalue)
            hashtable[1][new_hashvalue][columnName] = data 
            print("record Updated")
        
        else:
            print("Item not found.")
        
    
def get(hashtable, key, size, collision_path, opNumber): # returns dictionary
    
    start = hash_function(key, size)    # First hashvalue calculated from the key
    pos = start    
    
    while hashtable[0][pos] != None:
        
        collision_path[opNumber].append(pos)
        
        if key == hashtable[0][pos]:
            return hashtable[1][pos]
    
        else:
            pos = collision_resolver(key, pos, size)
            
            if pos == start:     # If the whole hashtable is iterated / checked    
                break
    
    print("Item not found")
        
def delete(hashtable, key, size, collision_path, opNumber): #returns hashtable, size, prints a msg  'Item Deleted'
   
    hash_value = hash_function(key, size)
    new_hashvalue = hash_value
   
    # If a collision occurs:
    if hashtable[0][hash_value] != key:

        count = 1       # Variable to keep check if the whole hashtable is iterated / checked
        
        while hashtable[0][new_hashvalue] != key and count != size:
            
            collision_path[opNumber].append(new_hashvalue)
            new_hashvalue = collision_resolver(key, new_hashvalue, size)
            count += 1
        
        # If key is found:   
        if hashtable[0][new_hashvalue] == key:
            hashtable[0][new_hashvalue] = '#'
            hashtable[1][new_hashvalue] = '#'
            collision_path[opNumber].append(new_hashvalue)
            print("Item Deleted")
        
        # If key does not exist:
        else:
            print("Item not found.")
        
    # If no collision occurs:
    else:
        
        collision_path[opNumber].append(new_hashvalue)
        hashtable[0][new_hashvalue] = '#'
        hashtable[1][new_hashvalue] = '#'
        print("Item Deleted")
    
    # Downsizing if required:
    if loadFactor(hashtable, size) < 30 and loadFactor(hashtable, size) > 0:
        if size != 7:
            hashtable, size = resize_hashtable(hashtable, size, False)
  
    return hashtable, size
    
# Function to calculate the next prime number:  
def next_prime(n):
    num = n
    while True:
        s = num
        for i in range(2, num):
            if num % i == 0:
                num = num + 1
                break
        if num == s:
            return num
            
        
                
            