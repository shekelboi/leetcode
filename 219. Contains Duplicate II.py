def containsNearbyDuplicate(nums, k):
    # We should add the index where a number occurs to the dictionary
    # Next time the same number occurs, we should check if the distance is smaller than k
    # If it is, then return true
    # Else we add the current index of the item
    frequencies = {}

    for i, n in enumerate(nums):
        if n not in frequencies.keys():
            frequencies[n] = i
        else:
            if i - frequencies[n] <= k:
                return True
            else:
                frequencies[n] = i
    return False


nums = [1, 0, 1, 1]
k = 1
print(containsNearbyDuplicate(nums, k))
