from math import log10


def intToRoman(num):
    roman_dict = {
        1: "I",
        2: "II",
        3: "III",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    roman = []
    power = 0
    while num != 0:
        remainder = num % 10
        if remainder <= 3:
            roman.append(roman_dict[10 ** power] * remainder)
        elif remainder == 4:
            roman.append(roman_dict[10 ** power] + roman_dict[10 ** power * 5])
        elif remainder == 5:
            roman.append(roman_dict[10 ** power * 5])
        elif remainder <= 8:
            roman.append(roman_dict[10 ** power * 5] + roman_dict[10 ** power] * (remainder - 5))
        elif remainder == 9:
            roman.append(roman_dict[10 ** power] + roman_dict[10 ** (power + 1)])
        power += 1
        num //= 10
    return "".join(roman[::-1])


print(intToRoman(182))
