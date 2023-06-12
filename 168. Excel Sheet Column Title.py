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