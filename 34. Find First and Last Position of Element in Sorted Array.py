def searchRange(nums, target):
    found = False

    left_pointer = 0
    right_pointer = len(nums) - 1
    index = 0
    while not found:
        index = (left_pointer + right_pointer) // 2
        if nums[index] == target:
            found = True
        elif nums[index] < target:
            left_pointer = index + 1
        elif nums[index] > target:
            right_pointer = index - 1
    return index


nums = [3, 4, 6, 8, 9, 10, 13, 15, 16]
target = 3
print(searchRange(nums, target))