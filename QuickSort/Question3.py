# Function to perform quicksort
def partition(array, low, high, column):
    pivot = low
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j][column] <= array[pivot][column]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[pivot], array[i-1] = array[i - 1], array[pivot]
    pivot = i - 1
    return pivot

def partition_mid(array, low, high, column):
    pivot = low
    array[low], array[pivot] = array[pivot], array[low]
    return partition(array, low, high, column)

def quick_sort_rectangles(array, low, high, column):
    if low < high:
        pivot = partition_mid(array, low, high, column)
        print(array)
        quick_sort_rectangles(array, low, pivot - 1, column)
        quick_sort_rectangles(array, pivot + 1, high, column)



# Testing
rectangle_records  = [{"ID":"Rect1","Length": 40 ,"Breadth": 25 ,"Color":"red"} , {"ID":"Rect2","Length":30 ,"Breadth": 20 ,"Color":"blue"} , {"ID":"Rect3","Length": 70 ,"Breadth": 45 ,"Color":"green"} , {"ID":"Rect4","Length": 20 ,"Breadth": 10 ,"Color":"purple"}]
quick_sort_rectangles(rectangle_records, 0, len(rectangle_records)-1, "Length")

# Should print:
# [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]
# [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]