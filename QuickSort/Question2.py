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
    pivot = high
    array[low], array[pivot] = array[pivot], array[low]
    return partition(array, low, high, column)

def quick_sort_by_column_number(array, low, high, column):
    if low < high:
        pivot = partition_mid(array, low, high, column)
        print(array)
        quick_sort_by_column_number(array, low, pivot - 1, column)
        quick_sort_by_column_number(array, pivot + 1, high, column)


# Testing
matrix = [['square', 'rectangle', 'triangle'],['chair', 'table', 'house'],['motor cycle', 'car', 'truck']]
quick_sort_by_column_number(matrix, 0, 2, 1)

# Should print:
# [['motor cycle', 'car', 'truck'], ['chair', 'table', 'house'], ['square', 'rectangle', 'triangle']]
# [['motor cycle', 'car', 'truck'], ['square', 'rectangle', 'triangle'], ['chair', 'table', 'house']]

matrix = [[75, 28, 12], [63, 37, 23], [84, 15, 49]]
quick_sort_by_column_number(matrix,0, 2, 1)

# Should print:
# [[84, 15, 49], [63, 37, 23], [75, 28, 12]]
# [[84, 15, 49], [75, 28, 12], [63, 37, 23]]