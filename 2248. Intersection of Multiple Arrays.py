def intersection(nums):
    occurences = {}
    for numb in nums[0]:
        occurences[numb] = len(nums) - 1
        for rest in nums[1:]:
            if numb not in rest:
                break
            else:
                occurences[numb] -= 1

    return sorted([k for k, v in occurences.items() if v == 0])


nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection(nums))
