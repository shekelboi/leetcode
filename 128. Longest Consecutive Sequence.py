def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    sequence_dict = {}
    for n in nums:
        if n not in sequence_dict:
            sequence_dict[n] = 1
            if n + 1 in sequence_dict and sequence_dict[n + 1] is not None:
                sequence_dict[n] += sequence_dict[n + 1]
                sequence_dict[n + 1] = None

    for k, v in sequence_dict.items():
        while v is not None and k + v in sequence_dict and sequence_dict[k + v] is not None:
            sequence_dict[k] += sequence_dict[k + v]
            sequence_dict[k + v] = None
            v = sequence_dict[k]

    print(sequence_dict)
    return max([v for v in sequence_dict.values() if v is not None])


nums = [1, 2, 0, 1]
print(longestConsecutive(nums))
