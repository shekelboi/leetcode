def containsNearbyDuplicate(nums, k):
    frequencies = {}

    for n in nums:
        if n not in frequencies.keys():
            frequencies[n] = 1
        else:
            frequencies[n] += 1

    for i in range(len(nums) - 1):
        if frequencies[nums[i]] == 2:
            for j in range(i + 1, len(nums)):
                if abs(i - j) <= k and nums[i] == nums[j]:
                    return True
    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))
