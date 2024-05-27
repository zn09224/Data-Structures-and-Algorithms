from Question3 import *

def RemoveFromStart(list):
    if IsEmpty(list) == True:
        return "List is empty"
    else:
        for i in range(0, NumberOfElements(list)-1):
            a=list[i]
            list[i] = list[i+1]
            list[i+1]=a
        list[NumberOfElements(list)-1] = None
        return "Element removed successfully"


if __name__ == "__main__":
    
    print(RemoveFromStart([None,None]))
    solution = "List is empty"
    print(RemoveFromStart(['a','b']))
    ListADT = ["b",None]
    solution = "Element removed successfully"
