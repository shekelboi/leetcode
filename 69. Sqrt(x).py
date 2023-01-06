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


def my_sqrt_two_pointers(x):
    left, right = 0, 2 ** 32
    while left < right:
        mid = (left + right) // 2
        # print(f"{left} {mid} {right}")
        res = mid ** 2
        if res == x or left == mid:
            return mid
        elif res < x:
            left = mid
        elif res > x:
            right = mid


x = 15
print(my_sqrt_two_pointers(x))
