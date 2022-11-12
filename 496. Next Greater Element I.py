def nextGreaterElement(nums1, nums2):
    return [next((n2 for n2 in nums2[nums2.index(n)::] if n2 > n), -1) for n in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))