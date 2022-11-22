import re

INT_MIN = -(2 ** 31) - 1
INT_MAX = 2 ** 31 - 1


def myAtoi(s):
    match = re.search(r"(?P<characters>[^\s\d\-+]*)\s*(?P<sign>[-+]*)(?P<digits>\d+)", s)
    if match is None or match.group("digits") is None or (
            match.group("sign") is not None and len(match.group("sign")) > 1) or match.group(
        "characters") is not None and match.group("characters") != "":
        return 0

    digits = int(match.group("digits"))
    if match.group("sign") is not None and match.group("sign") == "-":
        digits *= -1

    if digits > INT_MAX:
        return INT_MAX
    elif digits < INT_MIN:
        return INT_MIN

    return digits


print(myAtoi("+-12"))
