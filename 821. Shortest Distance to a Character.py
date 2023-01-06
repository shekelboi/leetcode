def shortestToChar(s, c):
    indexes = []
    for i, char in enumerate(s):
        if char == c:
            indexes.append(i)

    res = []

    for i in range(len(s)):
        min_index = min([abs(i - index) for index in indexes])
        res.append(min_index)

    return res


s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
