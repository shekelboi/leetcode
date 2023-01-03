def sumOddLengthSubarrays(arr):
    result = 0
    for i in range(1, len(arr) + 1, 2):
        for j in range(len(arr) - (i - 1)):
            for k in range(i):
                result += arr[j + k]
                print(arr[j + k], end=" ")
            print()
        print()
    return result


arr = [1, 4, 2, 5, 3]
print(sumOddLengthSubarrays(arr))
