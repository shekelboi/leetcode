# Exact opposite of what needs to be done
# def convertToTitle(columnNumber: int) -> str:
#     num_value = ord('A') - 1
#     res = 0
#     for i, v in enumerate(columnNumber):
#         base = 26 ** i
#         res += base * v
#     return res
#
#
# columnNumber = 28

def convertToTitle(columnNumber: int) -> str:
    num_value = ord('A')
    output = ''
    while columnNumber != 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        output += chr(num_value + remainder)
        columnNumber //= 26
    return output[::-1]


columnNumber = 28
print(convertToTitle(columnNumber))