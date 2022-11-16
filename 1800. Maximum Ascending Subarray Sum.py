def maxAscendingSum(nums):
    total = nums[0]
    max_total = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            total += nums[i]
        else:
            total = nums[i]
        if max_total < total:
            max_total = total
    return max_total


nums = [10, 20, 30, 5, 10, 50]
print(maxAscendingSum(nums))
