def reverseOnlyLetters(s):
    output = [c for c in s]
    letters = list(reversed([c for c in output if c.isalpha()]))
    for i, c in enumerate(output):
        if c.isalpha():
            output[i] = letters.pop(0)
    return "".join(output)


s = "ab-cd"
print(reverseOnlyLetters(s))
