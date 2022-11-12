def concatenatedBinary(n):
    concat = ""
    for i in range(1, n + 1):
        concat += str(bin(i)[2:])
    res = int(concat, 2)
    if res > 10 ** 9:
        return res % (10 ** 9 + 7)
    else:
        return res


print(concatenatedBinary(12))