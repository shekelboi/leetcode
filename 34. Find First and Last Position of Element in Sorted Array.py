def searchRange(nums, target):
    minimum = -1
    maximum = -1
    for i, n in enumerate(nums):
        if n == target:
            if minimum == -1:
                minimum = i
            maximum = i
    return [minimum, maximum]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
