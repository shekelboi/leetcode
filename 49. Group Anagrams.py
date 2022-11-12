import json
import os
from itertools import permutations


# # With permutations
# def groupAnagrams(strs):
#     found = []
#     for word in strs:
#         perms = ["".join(p) for p in permutations([c for c in word])]
#         if not any(word in f for f in found):
#             found.append([s for s in strs if s in perms])
#     return found

def str_to_dict(input):
    dic = {}
    for c in input:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 0
    return dic


def are_anagrams(str1, str2):
    if len(str1) is not len(str2):
        return False
    return str_to_dict(str1) == str_to_dict(str2)


def groupAnagrams(strs):
    groups = []
    for word in strs:
        if not any(word in g for g in groups):
            group = [s for s in strs if are_anagrams(word, s)]
            groups.append(group)
    return groups


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["bdddddddddd", "bbbbbbbbbbc"]
strs = json.loads(os.environ["task_49"])
print(len(strs))
print(groupAnagrams(strs))
