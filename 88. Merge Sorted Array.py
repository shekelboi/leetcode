def merge(nums1, m, nums2, n):
    if n == 0:
        return nums1

    for i in range(m):
        if nums2[0] < nums1[i]:
            # Swap the two elements
            temp = nums1[i]
            nums1[i] = nums2[0]
            nums2[0] = temp

            # Sort nums2
            for i in range(n - 1):
                if nums2[i] > nums2[i + 1]:
                    temp = nums2[i]
                    nums2[i] = nums2[i + 1]
                    nums2[i + 1] = temp
                else:
                    break  # Since it's already in ascending order

    for i in range(n):
        nums1[m + i] = nums2[i]
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = len([n for n in nums1 if n != 0])
nums2 = [2, 5, 6]
n = len(nums2)
print(merge(nums1, m, nums2, n))
