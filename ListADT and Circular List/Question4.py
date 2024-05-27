from Question2 import *

def InsertAtStart(list, element):
    if IsFull(list) == True:
        return "List is full"
    else:
        for i in range(NumberOfElements(list) - 1, -1, -1):
            a = list[i]
            list[i] = None
            list[i+1] = a
        Set(list,0,element)
        return "Element inserted successfully"
         
        


if __name__ == "__main__":
    print(InsertAtStart([None,None],'a'))
    ListADT = ["a",None]
    solution = "Element inserted successfully"

    print(InsertAtStart(['a','b'],'c'))
    solution = "List is full"
