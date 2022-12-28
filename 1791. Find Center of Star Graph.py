def findCenter(edges):
    for i in range(len(edges)):
        edges[i] = set(edges[i])

    return list(edges[0].intersection(*edges))[0]


edges = [[1, 2], [2, 3], [4, 2]]
print(findCenter(edges))
