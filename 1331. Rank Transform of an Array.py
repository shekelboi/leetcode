def arrayRankTransform(arr):
    ranks = sorted(list(set(arr)))
    return [ranks.index(a) + 1 for a in arr]


arr = [40, 10, 20, 30]
print(arrayRankTransform(arr))
