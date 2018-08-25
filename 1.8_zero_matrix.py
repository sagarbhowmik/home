"""
if an element in an MxN matrix is 0, its entire row and column are set to 0
"""

def setZero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    ret_matrix = [[None] * cols for i in range(0, rows)]
    #print ret_matrix
    for i in range(0, rows):
        for j in range(0,cols):
            if matrix[i][j] == 0:
                for c in range(0, cols):
                    ret_matrix[i][c] = 0
                for r in range(0, rows):
                    ret_matrix[r][j] = 0
            else:
                if ret_matrix[i][j] is None:
                    ret_matrix[i][j] = matrix[i][j]
    return ret_matrix

print setZero([[1,2, 3,4,5,6,7,8,9,10], [1,0,1,0,1,0,1,0,1,0], [1,1,1,1,1,1,1,1,1,1]])
print setZero([[1,1,1],[1,0,1],[1,1,1]])



