def Initialize(n):
    new_list = [None for i in range(n)]
    return new_list

def Get(list,index):
    my_value = list[index]
    return my_value

def Set(list,index,value):
    list[index] = value
    return list

def Size(list):
    return len(list)

def NumberOfElements(list):
    for i in range(len(list)):
        if list[i] == None:
            return i
    return len(list)

def IsEmpty(list):
    for i in range(len(list)):
        if list[i] != None:
            return False
    return True

def IsFull(list):
    for i in range(len(list)):
        if list[i] == None:
            return False
    return True


if __name__ == "__main__":
    print(Initialize(5))
    solution = [None,None,None,None,None]

    Set([10,None,None,None,None],0,10)
    solution = [10,None,None,None,None]

    print(Get([10,None,None,None,None],0))
    solution = 10

    print(Size([10,None,None,None,None]))
    solution = 5

    print(NumberOfElements([10,None,None,None,None]))
    solution = 1

    print(IsEmpty([10,None,None,None,None]))
    solution = False

    print(IsFull([10,None,None,None,None]))
    solution = False
    