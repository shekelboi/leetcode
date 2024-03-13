from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    nums_dict = Counter(nums)
    max_key = max(nums_dict.items(), key=lambda element: element[1])
    return max_key[0]


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))