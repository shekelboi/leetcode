import re

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


def myAtoi(s):
    res = re.search(r"([a-zA-Z]*)( *)(\-*[0-9]+)", s).groups()
    if res[0] is not "":
        return 0
    else:
        res = int(res[2])
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        else:
            return res


print(myAtoi("+-42"))
