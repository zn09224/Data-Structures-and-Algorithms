# This code is implemented using the algorithm taught in theory c

# def quick_sort(array, low, high):
    
#     if low < high:
#         pivot = partition(array, low, high)
#         print(array)
#         quick_sort(array, low, pivot - 1)
#         quick_sort(array, pivot + 1, high)

# def partition(array, low, high):
    
#     i = low
#     j = high
#     pivot = (i + j)//2    
#     while (i < j):
#         while (array[i] <= array[pivot]):
#             i = i + 1
#         while (array[j] > array[pivot]):
#             j = j - 1
#         if i < j:
#             array[i], array[j] = array[j], array[i]
#     array[j], array[pivot] = array[pivot], array[j]
#     return j

def partition(array, low, high):
    pivot = low
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[pivot], array[i-1] = array[i - 1], array[pivot]
    pivot = i - 1
    return pivot

def partition_mid(array, low, high):
    pivot = (low + high)//2
    array[low], array[pivot] = array[pivot], array[low]
    return partition(array, low, high)

def quick_sort(array, low, high):
    if low < high:
        pi = partition_mid(array, low, high)
        print(array)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

# Testing
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)

# Should print:
# [5, 7, 1, 8, 10, 9]
# [1, 5, 7, 8, 10, 9]
# [1, 5, 7, 8, 10, 9]
# [1, 5, 7, 8, 9, 10]