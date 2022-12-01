def removeElement(nums, val):
    right = 0  # Number of elements discarded from the right side of the array
    left = 0
    while left < len(nums) - right:
        right_index = len(nums) - 1 - right
        print(f"{nums[left]} {nums[right_index]}")
        if nums[right_index] == val:
            right += 1
        else:
            if nums[left] == val:
                nums[left] = nums[right_index]
                right += 1
            left += 1
    return len(nums) - right


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
