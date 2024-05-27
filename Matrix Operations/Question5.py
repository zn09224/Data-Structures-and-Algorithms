def initialize_matrix(rows,cols):
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    return matrix

def reduce_image(lst):

    matrix = initialize_matrix(len(lst), len(lst[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < len(lst) - 1:
                matrix[i][j] += lst[i+1][j]
            if j < len(lst[i]) - 1:
                matrix[i][j] += lst[i][j+1]
            if i > 0:
                matrix[i][j] += lst[i-1][j]
            if j > 0:
                matrix[i][j] += lst[i][j-1]
            if i > 0 and j > 0:
                matrix[i][j] += lst[i-1][j-1]
            if i < len(lst) - 1 and j > 0:
                matrix[i][j] += lst[i+1][j-1]
            if i > 0 and j < len(lst[i]) - 1:
                matrix[i][j] += lst[i-1][j+1]
            if i < len(lst) - 1 and j < len(lst[i]) - 1:
                matrix[i][j] += lst[i+1][j+1]
        
            matrix[i][j] = matrix[i][j] * lst[i][j]
            matrix[i][j] = matrix[i][j] ** (1/3)
            matrix[i][j] = round(matrix[i][j], 3)
    
    return matrix





print(reduce_image([[10, 20, 20], [10, 10, 10], [20, 10, 20]]))
# solution=[[7.368, 10.627, 9.283], [8.879, 10.627, 9.283], [8.434, 8.879, 8.434]]

# print(reduce_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# solution=[[2.224, 3.362, 3.391], [4.514, 5.848, 5.451], [4.919, 6.283, 5.55]]
