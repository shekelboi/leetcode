def isPalindrome(s):
    original = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
    return original == list(reversed(original))


print(isPalindrome("A man, a plan, a canal: Panama"))
