def wordPattern(pattern, s):
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    for i in range(len(words) - 1):
        for j in range(i, len(words)):
            is_equal = pattern[i] == pattern[j]
            if (words[i] == words[j]) != is_equal:
                return False
    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
