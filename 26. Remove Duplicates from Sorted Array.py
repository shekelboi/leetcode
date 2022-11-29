def removeDuplicates(nums):
    unique = 1
    left = 0
    right = left + 1
    while right < len(nums):
        if nums[left] != nums[right]:
            unique += 1
            left += 1
            nums[left] = nums[right]
        right += 1

    for i in range(unique, len(nums)):
        nums[i] = "_"

    return unique


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
