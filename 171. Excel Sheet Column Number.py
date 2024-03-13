# Exact opposite of what needs to be done
def titleToNumber(columnTitle: str) -> int:
    num_value = ord('A') - 1
    res = 0
    for i, v in enumerate(columnTitle[::-1]):
        base = 26 ** i
        res += base * (ord(v) - num_value)
    return res


columnNumber = 28
print(titleToNumber('AB'))