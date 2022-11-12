def updateMatrix(mat):
    output = [[j for j in i] for i in mat]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            output[i][j] = find_closest(mat, i, j)
    return output


def find_closest(mat, x, y):
    top_left = [x, y]
    bottom_right = [x, y]
    counter = 0
    if mat[x][y] == 0:
        return 0

    while not (top_left == [0, 0] and bottom_right == [len(mat) - 1, len(mat[0]) - 1]):
        if top_left[0] > 0:
            top_left[0] -= 1
        if top_left[1] > 0:
            top_left[1] -= 1
        if bottom_right[0] < len(mat) - 1:
            bottom_right[0] += 1
        if bottom_right[1] < len(mat[0]) - 1:
            bottom_right[1] += 1
        counter += 1

        minimum_distance = 9999999

        for i in range(top_left[1], bottom_right[1] + 1):
            if mat[top_left[0]][i] == 0:
                dist = distance([top_left[0], i], [x, y])
                if minimum_distance > dist:
                    minimum_distance = dist
            if mat[bottom_right[0]][i] == 0:
                dist = distance([bottom_right[0], i], [x, y])
                if minimum_distance > dist:
                    minimum_distance = dist

        for i in range(top_left[0], bottom_right[0] + 1):
            if mat[i][top_left[1]] == 0:
                dist = distance([i, top_left[1]], [x, y])
                if minimum_distance > dist:
                    minimum_distance = dist
            if mat[i][bottom_right[1]] == 0:
                dist = distance([i, bottom_right[1]], [x, y])
                if minimum_distance > dist:
                    minimum_distance = dist

        if minimum_distance != 9999999:
            top = x + minimum_distance if (x + minimum_distance) < len(mat) else len(mat) - 1
            bottom = x - minimum_distance if (x - minimum_distance) > 0 else 0
            for i in range(bottom, top):
                if mat[i][y] == 0:
                    dist = distance([i, y], [x, y])
                    if dist < minimum_distance:
                        minimum_distance = dist
            right = y + minimum_distance if (y + minimum_distance) < len(mat[0]) else len(mat[0]) - 1
            left = y - minimum_distance if (y - minimum_distance) > 0 else 0
            for i in range(left, right):
                if mat[x][i] == 0:
                    dist = distance([x, i], [x, y])
                    if dist < minimum_distance:
                        minimum_distance = dist
            return minimum_distance
    return -1


def distance(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])


mat = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
print(updateMatrix(mat))
