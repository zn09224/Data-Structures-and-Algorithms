def hash_function(key,size):
    
    if type(key) == int:
        return (key % size)
    
    if type(key) == str:
        
        sum = 0
        
        for i in key:
            sum = sum + ord(i)
        
        return (sum % size) 
            

def collision_resolver(key,size, iteration):
    
    hash_value = hash_function(key, size)
    return (hash_value + iteration) % size

if __name__ == "__main__":
    print(hash_function(5,10)) # Should print 5
    print(hash_function("Hello", 10)) # Should print 0
    print(collision_resolver(hash_function("Hello", 10),10,2)) # Should print 2