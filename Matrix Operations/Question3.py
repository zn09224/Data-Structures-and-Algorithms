def initialize_matrix(rows,cols):
    matrix = [[0 for i in range(rows)] for j in range(cols)]
    return matrix

def matrix_transpose(X):
    matrix = initialize_matrix(len(X), len(X[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = X[j][i]
    
    return matrix


# print(matrix_transpose([[12,7],[4 ,5],[3 ,8]]))
# solution=[[12, 4, 3],[7, 5, 8]]

# print(matrix_transpose([[12, 4, 3],[7, 5, 8]]))
# solution=[[12,7],[4 ,5],[3 ,8]]

