def reverse_int(x, is_negative):
    return int(str(x)[::-1]) if not is_negative else -int(str(x)[::-1])


def reverse(x):
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1
    digits = len(str(INT_MAX))
    is_negative = x < 0
    x = abs(x)
    if len(str(x)) < digits:
        return reverse_int(x, is_negative)
    elif len(str(x)) > digits or x in [INT_MIN, INT_MAX]:
        return 0
    else:
        for i, d in enumerate([int(c) for c in str(x)[::-1]]):
            int_min_current = int(str(abs(INT_MIN))[i])
            int_max_current = int(str(abs(INT_MAX))[i])
            if is_negative:
                if d < int_min_current:
                    return reverse_int(x, is_negative)
                elif d > int_min_current:
                    return 0
            else:
                if d < int_max_current:
                    return reverse_int(x, is_negative)
                elif d > int_max_current:
                    return 0
        return 0


print(reverse(2239999112))
