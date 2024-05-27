def sort_matrix_by_columnNumber(matrix, col):
    for i in range(len(matrix)):
        min = matrix[i][col]
        min_index = i
        for j in range(i + 1, len(matrix)):
            if matrix[j][col] < matrix[min_index][col]:
                min = matrix[j]
                min_index = j
        temp = matrix[i]
        matrix[i] = min
        matrix[min_index] = temp
    return matrix




# #Function call
# print(sort_matrix_by_columnNumber([['square', 'rectangle', 'triangle'],['chair','table', 'house'],['motor cycle', 'car', 'truck']], 2))

# #Expected output
# [['chair', 'table', 'house'], ['square', 'rectangle', 'triangle'], ['motor cycle', 'car', 'truck']]