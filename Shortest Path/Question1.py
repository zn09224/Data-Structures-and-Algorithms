def IsEmpty(queue):
    return queue == []




def DeQueue(queue):
    minimum = min(i[1] for i in queue)
    e = None
    for j in queue:
        if j[1] == minimum:
            e = j[0]
            queue.remove(j)
            return e



def EnQueue(queue, item, priority):
    count = 0
    for i, _ in queue:
        if i == item:
            queue[count] = item, priority
            return None
        count += 1
    queue.append((item, priority))

if __name__ == "__main__":
    queue = []
    EnQueue(queue,'A',1)
    EnQueue(queue,'B',2)
    EnQueue(queue,'C',3)
    EnQueue(queue,'D',4)
    EnQueue(queue,'E',5)
    EnQueue(queue,'F',6)
    EnQueue(queue,'G',7)
    print(queue)
    print(DeQueue(queue))
    print(queue)


    

