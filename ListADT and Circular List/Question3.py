from Question1 import *

def Remove(list, index):
    if IsEmpty(list) == True:
        return "List is empty"
    if index < 0 or index >= NumberOfElements(list):
        return "Invalid Index"
    else:
        for i in range(index, NumberOfElements(list)-1):
            list[i] = list[i+1]
        list[NumberOfElements(list)-1] = None
        return "Element removed successfully"


if __name__ == "__main__":
    print(Remove([10, 20, 30, 40, 50], 2))
    ListADT=[10, 20, 40, 50, None]
    solution = "Element removed successfully"

    print(Remove([10, 20, 40, 50, None], 0))
    ListADT=[20, 40, 50, None,None]
    solution = "Element removed successfully"

    print(Remove([20, 40, 50, None,None], 5))
    solution = "Invalid Index"

    print(Remove([None,None,None,None],0))
    solution= "List is empty"



