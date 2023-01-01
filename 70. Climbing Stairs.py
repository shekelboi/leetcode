def climbStairs(n):
    previous = 1
    current = 1
    for i in range(n - 1):
        print(current)
        temp = current
        current = current + previous
        previous = temp
    return current


print(climbStairs(4))
