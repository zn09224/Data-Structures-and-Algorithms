from Question1 import *

def Insert(list,index,value):
    print(list, index, Size(list))
    if IsFull(list) == True:
        return "List is full"
    elif index < 0 or index >= Size(list):
        return "Invalid Index"
    elif list[index] == None:
        Set(list,index,value)
        return "Element inserted successfully"
    else:
        for i in range(NumberOfElements(list)-1, index, -1):
            list[i-1] = list[i]
        Set(list,index,value)
        return "Element inserted successfully"
        
if __name__ == "__main__":
    print(Insert([None,None,None],0,'a'))
    solution = "Element inserted successfully"
    ListADT = ["a",None,None]

    print(Insert(["a",None,None],1,'b'))
    ListADT = ["a","b",None]
    solution = "Element inserted successfully"

    # print(Insert(["a","b",None],4,'e'))
    # solution = "Invalid Index"

    # print(Insert(["a","b",None],2,'c'))
    # ListADT = ["a","b","c"]
    # solution ="Element inserted successfully"

    # print(Insert(["a","b","c"],3,'d'))
    # solution="List is full"
    


    