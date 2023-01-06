def largestOddNumber(num: str):
    index = -1
    for i in reversed(range(len(num))):
        if int(num[i]) % 2 == 1:
            index = i
            break
    return "" if index == -1 else num[:i + 1]


num = "4206"
print(largestOddNumber(num))
