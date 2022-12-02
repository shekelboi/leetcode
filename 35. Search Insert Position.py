def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    if len(nums) == 1:
        return 0 if target <= nums[0] else 1
    while left < right:
        mid = (left + right) // 2
        # print(f"{left} {mid} {right}")
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid

    if target <= nums[right]:
        return right
    else:
        return right + 1


nums = [1, 3]
target = 3
print(searchInsert(nums, target))
