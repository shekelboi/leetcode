def threeSum(nums):
    triplets = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])

    triplets = [sorted(t) for t in triplets]
    unique_triplets = []
    for t in triplets:
        if t not in unique_triplets:
            unique_triplets.append(t)
    return unique_triplets


nums = [0, 0, 0]
print(threeSum(nums))
