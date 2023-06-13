def reverseBits(n: int) -> int:
    binary = bin(n)[2:]
    extra_zeros = ['0' for i in range(32 - len(binary))]
    binary = "".join([*extra_zeros, binary])
    return int("".join(binary[::-1]), 2)


n = 43261596
print(reverseBits(n))