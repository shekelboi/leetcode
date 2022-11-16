def longestPalindrome(s):
    def palindrome_check(s):
        if len(s) % 2 == 1:
            return s[:len(s) // 2] == s[len(s) // 2 + 1::][::-1]
        else:
            return s[:len(s) // 2] == s[len(s) // 2::][::-1]
    longest = ""
    if palindrome_check(s):
        return s
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            if palindrome_check(s[i:j]):
                if len(s[i:j]) > len(longest):
                    longest = s[i:j]
    return longest


print(longestPalindrome("a"))