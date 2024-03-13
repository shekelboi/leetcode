from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    elements_passed = set()
    for n in nums:
        if n not in elements_passed:
            elements_passed.add(n)
        else:
            return True
    return False