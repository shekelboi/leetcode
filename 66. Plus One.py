def plusOne(digits):
    digits[-1] += 1
    for i in reversed(range(len(digits))):
        if digits[i] >= 10:
            remainder = digits[i] % 10
            division = digits[i] // 10
            digits[i] = remainder
            if i == 0:
                digits.insert(0, division)
            else:
                digits[i - 1] += division
    return digits


digits = [9, 9]
print(plusOne(digits))
