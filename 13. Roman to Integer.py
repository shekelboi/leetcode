def romanToInt(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0

    counter = len(s) - 1
    while counter >= 0:
        if counter > 0 and roman_dict[s[counter - 1]] < roman_dict[s[counter]]:
            res += roman_dict[s[counter]] - roman_dict[s[counter - 1]]
            counter -= 1
        else:
            res += roman_dict[s[counter]]
        counter -= 1
    return res


print(romanToInt("MCMXCIV"))
