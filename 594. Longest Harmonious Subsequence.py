def findLHS(nums):
    occurences = {}
    for n in nums:
        if n not in occurences:
            occurences[n] = 1
        else:
            occurences[n] += 1

    longest = 0
    previous_key = sorted(occurences.keys())[0]

    for k in sorted(occurences.keys())[1:]:
        if abs(previous_key - k) == 1:
            current = occurences[previous_key] + occurences[k]
            longest = max(current, longest)
        previous_key = k

    return longest


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))
