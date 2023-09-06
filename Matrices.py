from random import randint

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

N = [
    [0, 5, 2],
    [3, 6, 1],
    [7, 4, 3]
    ]

J = [
    [0, 5],
    [3, 6],
    [7, 4]
    ]

def rotateClockwise(M):
    rows = len(M)
    cols = len(M[0])
    N = [([0] * rows) for i in range(cols)]
    for row in range(rows):
        for col in range(cols):
            N[col][rows-row-1] = M[row][col]
    return N

def mTranspose(M):
    dim = len(M)
    if dim != len(M[0]):
        print("Not Square")
        return
    N = [([0] * dim) for i in range(dim)]
    for row in range(dim):
        for col in range(dim):
            N[row][col] = M[col][row]
    return N

def mSum(M, N):
    rows = len(M)
    cols = len(M[0])
    S = mZeroes(rows, cols)
    for row in range(rows):
        for col in range(cols):
            S[row][col] = M[row][col] + N[row][col]

    return S

def mMultiply(M, N):
    rowsM = len(M)
    colsM = len(M[0])
    rowsN = len(N)
    colsN = len(N[0])
    if colsM != rowsN:
        print("Can't Multiply")
        return
    S = mZeroes(rowsM, colsN)
    for rowFinal in range(rowsM):
        for colFinal in range(colsN):
            tot = 0
            for index in range(colsM):
                tot += M[rowFinal][index]*N[index][colFinal]
            S[rowFinal][colFinal] = tot
    return S

def mZeroes(x, y):
    return [([0] * y) for i in range(x)]

def mScale(M, n):
    rows = len(M)
    cols = len(M[0])
    N = mZeroes(rows, cols)
    for i in range(rows):
        for j in range(cols):
            N[i][j] = n * M[i][j]
    return N

def genP(rows):
    nums = list(range(rows))
    indicesUnordered = []
    for i in range(rows):
        index = randint(0, len(nums)-1)
        indicesUnordered += [nums[index]]
        nums.remove(nums[index])
    P = []
    
    for i in range(rows):
        row = []
        for j in range(rows):
            if j == indicesUnordered[i]:
                row.append(1)
            else:
                row.append(0)
        P.append(row)
    return P

def printMatrix(M):
    rows = len(M)
    cols = len(M[0])
    for i in range(rows):
        print(M[i])
