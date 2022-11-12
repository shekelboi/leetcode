def calculate_value(s):
    stack = []
    for c in s:
        if c == "#":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


def backspaceCompare(s, t):
    print(calculate_value(s))
    print(calculate_value(t))
    return calculate_value(s) == calculate_value(t)


s = "y#fo##f"
t = "y#f#o##f"
arr = []
print(backspaceCompare(s, t))