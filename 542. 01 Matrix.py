def updateMatrix(mat):
    mat = [[0 if j == 0 else None for j in i] for i in mat]
    counter = 0
    inserted = []
    for x, arr in enumerate(mat):
        for y, el in enumerate(arr):
            if mat[x][y] == counter:
                inserted.extend(put_around(mat, counter + 1, x, y))

    while any(None in arr for arr in mat):
        swap = []
        counter += 1
        for i in inserted:
            swap.extend(put_around(mat, counter + 1, i[0], i[1]))
        inserted = swap
    return mat


def put_around(mat, counter, x, y):
    arr = []
    bottom = x - 1
    if bottom >= 0 and mat[bottom][y] is None:
        mat[bottom][y] = counter
        arr.append([bottom, y])
    top = x + 1
    if top < len(mat) and mat[top][y] is None:
        mat[top][y] = counter
        arr.append([top, y])
    left = y - 1
    if left >= 0 and mat[x][left] is None:
        mat[x][left] = counter
        arr.append([x, left])
    right = y + 1
    if right < len(mat[0]) and mat[x][right] is None:
        mat[x][right] = counter
        arr.append([x, right])
    return arr


# mat = [
#     [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
#     [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
#     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
#     [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
# ]
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))
