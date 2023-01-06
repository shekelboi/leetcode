from collections import Counter


def canConstruct(ransomNote, magazine):
    letters = Counter(magazine)

    for c in ransomNote:
        if c in letters and letters[c] > 0:
            letters[c] -= 1
        else:
            return False

    return True


ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
