import numpy as np
c = 0
res = 0
f = open("input.txt","r")
out = open("output.txt","w")
iplines = f.readlines()
lines = [x.strip() for x in iplines]
n = int(lines[0])
a = np.zeros(shape=(n,n),dtype=np.int64)
scoot = int(lines[2])
tscoot = scoot * 12

for line in lines[3:tscoot+3]:
    ind = line.split(',')
    i = int(ind[0])
    j = int(ind[1])
    a[i][j] = a[i][j] + 1

officers = int(lines[1])

def replacePos(b, row, col):
    for i in range(n):
        b[row][i] = -1
        b[i][col] = -1
        for j in range(n):
            if abs(i - row) == abs(j - col):
                b[i][j] = -1


def counter(array):
    val = np.argmax(array)
    i = val / n
    j = val % n
    cop[i][j] = 0
    return val


def isSafePos(grid, row, col):
    for i in range(n):
        if grid[row][i] == 1 or grid[i][col] == 1:
            return False

    for i in range(n):
        for j in range(n):
            if abs(i - row) == abs(j - col) and (grid[i][j] == 1):
                return False
    return True


def solution(grid, col):
    global c
    global res
    if c > res and col == n:
        res = c
        return
    if col == n:
        return
    for x in range(0, n):
            if isSafePos(grid, x, col):
                grid[x][col] = 1
                c += a[x][col]
                solution(grid, col+1)
                grid[x][col] = 0
                c -= a[x][col]


if officers == 1:
    count = np.max(a)
    out.write("%i" % (count))

elif officers < n:
    res = 0
    cop = np.copy(a)
    list = []
    for i in range(0, n*n):
        r = counter(cop)
        list.append(r)

    for index in list:
        b = np.copy(a)
        c = 0
        row = index/n
        col = index % n
        c += a[row][col]
        replacePos(b, row, col)
        for i in range(officers-1):
            val = np.argmax(b)
            i = val/n
            j = val % n
            c += a[i, j]
            replacePos(b,i,j)

        if c > res:
            res = c
    out.write("%i" % (res))
else:
    grid = np.zeros(shape=(n, n), dtype=np.int64)
    solution(grid, 0)
    out.write("%i" % (res))
