det = 1

def lud(M):
    rows = len(M)
    for i in range(rows):
        if rows != len(M[i]):
            return "Matrix not square"
    U = elim(M)

    global det

    for i in range(rows):
        det *= U[i][i]

    # reset for next use
    tempDet = det
    det = 1
    
    return tempDet

    
# elim uses a modified form of Gaussian elimination to get U
# (it doesn't change the matrix to RREF, and no swapping is allowed)
# for an L where main diagonal is all 1's

# (Note that LU = M, which is the whole point of LUD)

# UNLESS there's a zero as the pivot
# in which case it swaps a row in the original matrix
# and calls itself again
# and det is multiplied by -1

# Determinant of U is determinant of M because determinant of L is 1
# And the determinant of a product matrix is the same as the product
# Of the two determinants of the multiplier matricies

# My reference:
# https://www.youtube.com/watch?v=BFYFkn-eOQk&t=370s

def elim(M):
    global det
    rows = len(M)
    N = copySquare(M)
    for i in range(rows):
        for j in range(i+1, rows):
            if N[i][i] == 0:
                tempI = i
                while i <= rows:
                    if i == rows:
                        det = 0 # all zeroes below "pivot," so no solutions and det = 0(trivial proof)
                        return M
                    elif N[i][tempI] != 0:
                        det *= -1
                        return elim(swap(M, i, tempI))
                    i += 1
            temp = N[j][i]/N[i][i]
            for k in range(i, rows):
                N[j][k] -= temp*N[i][k]
    return N

# swaps two rows within a matrix
def swap(M, r1, r2):
    N = copySquare(M)
    temp = N[r1]
    N[r1] = N[r2]
    N[r2] = temp
    return N

# copies a square matrix
def copySquare(M):
    rows = len(M)
    N = [([0] * rows) for i in range(rows)]
    for i in range(rows):
        for j in range(rows):
            N[i][j] = M[i][j]
    return N
