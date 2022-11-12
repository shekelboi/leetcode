counter = 0


def recursive_solution(grid, x_len, y_len, k, path=None, x=0, y=0):
    global counter
    print(f"{counter}: {x},{y}")
    if path is None:
        path = []
    path.append((x, y))
    if x < x_len - 1:
        recursive_solution(grid, x_len, y_len, k, path[:], x + 1, y)
    if y < y_len - 1:
        recursive_solution(grid, x_len, y_len, k, path[:], x, y + 1)
    elif x == x_len - 1 and y == y_len - 1:
        if sum([grid[p_y][p_x] for p_x, p_y in path]) % k == 0:
            print(([grid[p_y][p_x] for p_x, p_y in path]))
            print(f"Path: {path}")
            counter += 1
        path = None
    return counter


def numberOfPaths(grid, k):
    x_len = len(grid[0])
    y_len = len(grid)
    return recursive_solution(grid, x_len, y_len, k)


# grid = [[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]]
# k = 1
# grid = [[5, 2, 4], [3, 0, 5], [0, 7, 2]]
# k = 3
grid = [[0, 0]]
k = 5
print(numberOfPaths(grid, k))
