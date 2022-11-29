def removeDuplicates(nums):
    number_of_duplicates = 0
    counter = 0
    while counter < len(nums) - 1 and nums[counter] != "_":
        if nums[counter] == nums[counter + 1]:
            number_of_duplicates += 1
            nums[counter + 1] = "_"
            for j in range(counter + 2, len(nums)):
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp
        else:
            counter += 1
    return len(nums) - number_of_duplicates


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
