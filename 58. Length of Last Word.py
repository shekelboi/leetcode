import re


def lengthOfLastWord(s):
    return len(s.split()[-1])


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
