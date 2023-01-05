def find_max_k_naive(nums):
    found = -1
    nums = sorted(nums, reverse=True)
    for n in nums:
        if -n in nums:
            return n
    return found


def find_max_k_optimized(nums):
    nums_set = set()
    max_num = -1
    for n in nums:
        inverse = -1 * n
        if inverse not in nums_set:
            nums_set.add(n)
        else:
            val = abs(n)
            if val > max_num:
                max_num = val
            nums_set.remove(inverse)

    return max_num


nums = [-1, 2, -3, 3]
print(find_max_k_optimized(nums))
