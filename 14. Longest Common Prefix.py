def longestCommonPrefix(strs):
    res = ""
    for i in range(min([len(s) for s in strs])):
        chars = [s[i] for s in strs]
        if len(set(chars)) == 1:
            res += chars[0]
        else:
            return res
    return res


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
