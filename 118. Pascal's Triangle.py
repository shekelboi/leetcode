def generate(numRows):
    pascal = []
    for i in range(min(numRows, 2)):
        pascal.append([])
        for j in range(i + 1):
            pascal[i].append(1)

    for i in range(numRows)[2:]:
        pascal.append([1])
        for j in range(len(pascal[i - 1]) - 1):
            pascal[i].append(sum(pascal[i - 1][j:j + 2]))
        pascal[i].append(1)

    return pascal


numRows = 5
print(generate(numRows))
