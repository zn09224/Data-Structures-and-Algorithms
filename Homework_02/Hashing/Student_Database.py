from HashTable import *
import csv

def create_studentDatabase(studentRecords):
    
    size = 7
    hashtable = create_hashtable(size)     # Initializing hashtable of size = 7
    
    for i in studentRecords:
        hashtable, size = put(hashtable, i["ID"], i, size)      # Putting the given data in hashtable
    
    return hashtable

def perform_Operations(hashtable, operationFile):
    
    # Reading the given file and converting in appropriate format:
    with open (operationFile) as f:
        lines = f.readlines()
        
    input = []
    for line in lines :
        line = line.strip("/n") 
        tokens = line.split() 
        input.append(tokens)
    
    size = len(hashtable[0])        # Getting the size of our hashtable from the length of keys list
    
    collision_path = {}     # Initializing collision path dictionary
    
    opNumber = 0        # Operation Number starting from 0
    
    for operation in input:
        
        opNumber += 1
        
        collision_path[opNumber] = []
        
        # If whole value dictionary is to be found:
        if len(operation) == 2 and operation[0] == "Find":
            print(get(hashtable, operation[1], size, collision_path, opNumber))
        
        # If some specific value from the value dictionary is to be found:
        elif len(operation) == 3 and operation[0] == "Find":
            print(get(hashtable, operation[1], size, collision_path, opNumber)[operation[2]])
            
        # If some value needs to be updated:
        elif operation[0] == "Update":
            Update(hashtable, operation[1], operation[2], operation[3], size, collision_path, opNumber)
        
        # If some key and value needs to be deleted:
        elif operation[0] == "Delete":
            hashtable, size = delete(hashtable, operation[1], size, collision_path, opNumber)
        
        
    return collision_path
            


            

def main(filename):
    
    # Reading the given file and converting in appropriate format:
    with open (filename) as f :
        lines = f.readlines()
        
    input = []
    for line in lines :
        line = line.strip("/n") 
        tokens = line.split() 
        input.append(tokens)
    
    result = [[sublist[0].split(',')] for sublist in input]         # Splitting by comma and creating nested lists         
    
    students = []       # List of all students
    for i in range(1, len(result)):
        student = {}
        for j in range(len(result[0][0])):
            student[result[0][0][j]] = result[i][0][j]
        students.append(student)

    return students 

        
        
        

studentRecords=main('data.csv')
H=create_studentDatabase(studentRecords)
print(perform_Operations(H, 'Operations.txt'))
