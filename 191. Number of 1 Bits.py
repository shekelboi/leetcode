def hammingWeight(n: int) -> int:
    return sum([int(i) for i in bin(n)[2:]])


n = 11
print(hammingWeight(n))