from collections import Counter


def maximumSubarraySum(nums, k):
    k_dict = Counter(nums[:k])
    previous_sum = sum([(key * v) for (key, v) in k_dict.items()])
    greatest_sum = 0 if len(k_dict.keys()) != k else previous_sum

    for i in range(k, len(nums)):
        # Removing the previous element
        previous_element = nums[i - k]
        if k_dict[previous_element] == 1:
            del k_dict[previous_element]
        else:
            k_dict[previous_element] -= 1

        current_sum = previous_sum
        current_sum -= previous_element

        # Adding the next element
        next_element = nums[i]
        if next_element in k_dict:
            k_dict[next_element] += 1
        else:
            k_dict[next_element] = 1

        current_sum += next_element

        if current_sum > greatest_sum and len(k_dict.keys()) == k:
            greatest_sum = current_sum

        previous_sum = current_sum

    return greatest_sum


nums = [1, 2, 2]
k = 2
print(maximumSubarraySum(nums, k))