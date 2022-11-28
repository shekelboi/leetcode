def isValid(s):
    left = ["{", "(", "["]
    right = ["}", ")", "]"]

    parentheses = []

    for p in s:
        if p in right:
            if len(parentheses) != 0 and parentheses[-1] in left:
                if left[right.index(p)] == parentheses[-1]:
                    parentheses.pop()
                else:
                    return False
            else:
                return False
        else:
            parentheses.append(p)

    return len(parentheses) == 0


s = "[()(){([]{})}]"
print(isValid(s))
