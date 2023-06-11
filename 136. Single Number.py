from typing import List


def singleNumber(nums: List[int]) -> int:
    num_set = set()
    for n in nums:
        if n not in num_set:
            num_set.add(n)
        else:
            num_set.remove(n)
    return num_set.pop()


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))