def print_circular_array(array):
    row = len(array[0])
    col = len(array)
    r , c = 0, 0
    while r < row and c < col:
        for i in range(c, col):
            print array[r][i],
        r += 1

        for j in range(r, row):
            print array[j][col - 1],
        col -= 1

        if r < row:
            for k in range(col - 1, c - 1, -1):
                print array[row - 1][k],
            row -= 1

        if c < col:
            for l in range(row - 1, r - 1, -1):
                print array[l][c],
            c += 1


print_circular_array([['a','b','c','d'], ['l','m','n','e'], ['k','p','o','f'], ['j','i','h','g']])