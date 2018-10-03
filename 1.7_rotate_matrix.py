def rotateMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # check for null matrix or a non square matrix
    if rows == 0 or rows != cols:
        print "cannot rotate this matrix"
        exit()
    for layer in range(rows/2):
        first = layer
        last = rows - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            # left to top
            matrix[first][i] = matrix[last - offset][first]

            # bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right to bottom
            matrix[last][last - offset] = matrix[i][last]

            # top to bottom
            matrix[i][last] = top

    return matrix


"""
1 2 3           7 4 1
4 5 6   ===>    8 5 2
7 8 9           9 6 3
"""
print rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

"""
0 1 2 3          C 8 4 0 
4 5 6 7  ===>    D 9 5 1
8 9 A B          E A 6 2
C D E F          F B 7 3
"""
print rotateMatrix([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'A', 'B'], ['C', 'D', 'E', 'F']])


