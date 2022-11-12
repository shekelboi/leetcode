def updateMatrix(mat):
    mat = [[0 if j == 0 else None for j in i] for i in mat]
    counter = 0
    while any(None in arr for arr in mat):
        for x, arr in enumerate(mat):
            for y, el in enumerate(arr):
                if mat[x][y] == counter:
                    put_around(mat, counter + 1, x, y)
        counter += 1
    return mat


def put_around(mat, counter, x, y):
    bottom = x - 1
    if bottom >= 0 and mat[bottom][y] is None:
        mat[bottom][y] = counter
    top = x + 1
    if top < len(mat) and mat[top][y] is None:
        mat[top][y] = counter
    left = y - 1
    if left >= 0 and mat[x][left] is None:
        mat[x][left] = counter
    right = y + 1
    if right < len(mat[0]) and mat[x][right] is None:
        mat[x][right] = counter


mat = [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix(mat))
