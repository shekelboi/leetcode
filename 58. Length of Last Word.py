import re


def lengthOfLastWord(s):
    res = re.search(r"(\w*)\s*$", s)
    return res.group(1)


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
