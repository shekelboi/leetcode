def applyOperations(nums):
    arr = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            if nums[i] != 0:
                arr.append(nums[i])
            nums[i + 1] = 0
        else:
            if nums[i] != 0:
                arr.append(nums[i])
    arr.append(nums[-1])

    for i in range(len(nums) - len(arr)):
        arr.append(0)

    return arr


nums = [847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]
print(applyOperations(nums))
