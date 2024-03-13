def isMonotonic(nums):
    is_increasing = None
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff > 0:
            if is_increasing is not None and not is_increasing:
                return False
            is_increasing = True
        if diff < 0:
            if is_increasing is not None and is_increasing:
                return False
            is_increasing = False
    return True


nums = [1, 2, 2, 3]
print(isMonotonic(nums))
