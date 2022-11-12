def findPairs(nums, k):
    pairs = []
    for index_i, i in enumerate(nums[:-1]):
        for index_j, j in enumerate(nums[index_i + 1::], index_i + 1):
            if abs(i - j) == k:
                if (i, j) not in pairs and (j, i) not in pairs:
                    pairs.append((i, j))
    return len(pairs)


nums = [1, 3, 1, 5, 4]
k = 0
print(findPairs(nums, k))
