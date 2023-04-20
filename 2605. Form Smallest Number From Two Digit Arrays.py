def minNumber(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    common = nums1.intersection(nums2)
    if common:
        return min(common)

    mins = sorted([min(nums1), min(nums2)])

    return int("".join(map(str, mins)))


nums1 = [4, 1, 3]
nums2 = [5, 7]
print(minNumber(nums1, nums2))