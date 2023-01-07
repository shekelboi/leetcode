def getRow(rowIndex):
    rowIndex += 1
    pascal = []
    for i in range(min(rowIndex, 2)):
        pascal.append([])
        for j in range(i + 1):
            pascal[i].append(1)

    for i in range(rowIndex)[2:]:
        pascal.append([1])
        for j in range(len(pascal[i - 1]) - 1):
            pascal[i].append(sum(pascal[i - 1][j:j + 2]))
        pascal[i].append(1)

    return pascal[-1]


rowIndex = 3
print(getRow(rowIndex))
