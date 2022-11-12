def lengthOfLongestSubstring(s):
    sub_string_arr = []
    longest_substring = []
    start = 0
    i = 0
    while i < len(s):
        if s[i] not in sub_string_arr:
            sub_string_arr.append(s[i])
            i += 1
        else:
            if len(sub_string_arr) > len(longest_substring):
                longest_substring = sub_string_arr
            start = start + 1
            i = start
            sub_string_arr = []
    if len(sub_string_arr) > len(longest_substring):
        longest_substring = sub_string_arr
    return len(longest_substring)


s = "dvdf"
print(lengthOfLongestSubstring(s))
