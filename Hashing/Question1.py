def create_hashtable(size): # returns tuple(list,list)
    
    return ([None for _ in range(size)], [None for _ in range(size)])

if __name__ == "__main__":
    print(create_hashtable(5))
    # Shoud print ([None, None, None, None, None], [None, None, None, None, None])