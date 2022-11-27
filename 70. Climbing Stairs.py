def climbStairs(n):
    results = [[1 for i in range(n)]]
    max_number_of_twos = n // 2
    for i in range(1, max_number_of_twos + 1):
        arr = [2 for j in range(i)]
        arr.extend([1 for j in range(n - i * 2)])
        results.append(arr)
    return results


print(climbStairs(10))
