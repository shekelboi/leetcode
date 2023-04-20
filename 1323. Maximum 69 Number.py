from math import log10, floor


def maximum69Number(num: int) -> int:
    number_of_digits = floor(log10(num))
    original_number = num
    while num > 0:
        divisor = 10 ** number_of_digits
        quotient = num // divisor

        if quotient == 6:
            original_number += 3 * divisor
            break

        num %= divisor
        number_of_digits -= 1
    return original_number


print(maximum69Number(9969))