from collections import Counter


# def findAnagrams(s, p):
#     len_p, len_s = len(p), len(s)
#     indices = []
#     anagram_dict = Counter(p)
#     string_dict = {}
#
#     for i, c in enumerate(s):
#         if c not in string_dict:
#             string_dict[c] = {i}
#         else:
#             string_dict[c].add(i)
#
#     for i in range(len_s - len_p + 1):
#         window = s[i:i + len_p]
#         if Counter(window) == anagram_dict:
#             indices.append(i)
#     return indices


def findAnagrams(s, p):
    indices = []
    anagram_dict = Counter(p)
    current_dict = Counter(s[0:len(p)])
    previous_index = 0
    if anagram_dict == current_dict:
        indices.append(previous_index)
    for i in range(previous_index + len(p), len(s)):
        current_dict[s[previous_index]] -= 1
        if current_dict[s[previous_index]] == 0:
            del current_dict[s[previous_index]]
        if s[i] in current_dict:
            current_dict[s[i]] += 1
        else:
            current_dict[s[i]] = 1
        if current_dict == anagram_dict:
            indices.append(previous_index + 1)
        previous_index += 1
    return indices


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
