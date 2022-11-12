def calculate_result(s: str):
    s = s[::-1]
    res = ""
    ignore_counter = 0
    for c in s:
        if c == "#":
            ignore_counter += 1
        elif ignore_counter > 0:
            ignore_counter -= 1
            continue
        else:
            res += c
    return res[::-1]


def backspaceCompare(s, t):
    return calculate_result(s) == calculate_result(t)


print(calculate_result("o###c"))
