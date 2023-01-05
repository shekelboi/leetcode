def find_max_k_naive(nums):
    found = -1
    nums = sorted(nums, reverse=True)
    for n in nums:
        if -n in nums:
            return n
    return found


nums = [-1, 2, -3, 3]
print(find_max_k_naive(nums))
