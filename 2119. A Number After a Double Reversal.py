def isSameAfterReversals(num):
    return int(str(int(str(num)[::-1]))[::-1]) == num


num = 1800
print(isSameAfterReversals(num))
