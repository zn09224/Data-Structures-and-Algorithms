def initialize_matrix(rows,cols):
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    return matrix

def matrix_multiplication(X, Y):
    error = "The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication."
    for i in range(len(X)):
        for j in range(len(X[i])):
            if len(X[i]) != len(Y):
                return error

    matrix = initialize_matrix(len(X), len(Y[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(X[0])):
                matrix[i][j] += (X[i][k] * Y[k][j])
    return matrix
            



# print(matrix_multiplication([[12,7,3],[4 ,5,6],[7 ,8,9]], [[5,8,1,2],[6,7,3,0], [4,5,9,1]]))
# solution=[[114, 160, 60, 27],[74, 97, 73, 14],[119, 157, 112, 23]]

# print(matrix_multiplication([[34,1,77],[2,14,8],[3 ,17,11]], [[6,8,1],[9,27,5],[2,43,31]]))
# solution=[[367, 3610, 2426], [154, 738, 320], [193, 956, 429]]

# print(matrix_multiplication([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))
# solution=[[58, 64], [139, 154]]

# print(matrix_multiplication([[7,3], [2,5], [6,8], [9,0]], [[8,14,0,3,-1], [7,11,5,91,3], [8,-4,19,5, 57]]))
# solution="The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication."
