def maxProductDifference(nums):
    def prod(arr):
        if len(arr) == 0:
            return 0
        res = arr[0]
        for n in arr[1:]:
            res *= n
        return res

    ARR_LEN = 2
    min_arr = []
    max_arr = []

    for n in nums:
        min_arr.append(n)
        min_arr.sort()
        min_arr = min_arr[:ARR_LEN]
        max_arr.append(n)
        max_arr.sort(reverse=True)
        max_arr = max_arr[:ARR_LEN]

    return prod(max_arr) - prod(min_arr)


nums = [5, 6, 2, 7, 4]
print(maxProductDifference(nums))
