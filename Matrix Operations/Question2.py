def initialize_matrix(rows,cols):
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    return matrix

def matrix_subtraction(X, Y):

    error = "Matrices A and B don't have the same dimension required for matrix subtraction."
    if len(X) == len(Y):
        for i in range(len(X)):
            if len(X[i]) != len(Y[i]):
                return error
    else:
        return error

    matrix = initialize_matrix(len(X), len(X[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = X[i][j] - Y[i][j]
    
    return matrix
    



# print(matrix_subtraction([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]))
# solution=[[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]

# print(matrix_subtraction([[12,7,3],[4,5,6],[7,8,9]],[[5,8,1],[6,7,3],[4,5,9]]) )
# solution=[[7,-1,2],[-2,-2,3],[3,3,0]]

# print(matrix_subtraction([[1],[1],[1]],[[2],[2],[4]]))
# solution=[[-1],[-1],[-3]]

# print(matrix_subtraction([[1],[2]],[[3,5],[4,6]]))
# solution="Matrices A and B don't have the same dimension required for matrix subtraction."
