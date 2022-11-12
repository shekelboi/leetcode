def isHappy(n):
    nums = []
    while n != 1:
        if n in nums:
            return False
        nums.append(n)
        current_sum = sum([int(x) ** 2 for x in str(n)])
        n = current_sum
    return True


n = 19
print(isHappy(n))