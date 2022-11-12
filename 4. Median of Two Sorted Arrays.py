def findMedianSortedArrays(nums1, nums2):
    arr = []
    arr.extend(nums1)
    arr.extend(nums2)
    arr.sort()
    if len(arr) == 0:
        return 0
    elif len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2.0


nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))