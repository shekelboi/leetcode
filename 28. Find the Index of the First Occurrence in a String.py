def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))