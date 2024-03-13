import math


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    res = math.log(n, 2)
    return 2 ** int(res) == n


n = 16
print(isPowerOfTwo(n))