def mySqrt(x):
    # Using a while loop since the iterator would require too much memory in case of a for loop
    i = 0
    while i < 2 ** 31:
        res = i ** 2
        if res == x:
            return i
        if res > x:
            return i - 1
        i += 1


x = 8
print(mySqrt(x))
