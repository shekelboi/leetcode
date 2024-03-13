from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    nums.append(None)
    ranges = []
    last = []
    for n in nums:
        if len(last) == 0:
            last = [n]
        elif last[-1] + 1 == n:
            if len(last) == 1:
                last.append(n)
            else:
                last[-1] += 1
        else:
            ranges.append("->".join([str(i) for i in last]))
            last = [n]

    return ranges


nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))