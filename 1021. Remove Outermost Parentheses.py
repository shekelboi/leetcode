def removeOuterParentheses(s):
    counter = 0
    decomp = []
    parenthesis = ""
    for c in s:
        if c == "(":
            counter += 1
        else:
            counter -= 1

        parenthesis += c

        if counter == 0:
            decomp.append(parenthesis)
            parenthesis = ""

    decomp = [d[1:len(d) - 1] for d in decomp]
    return "".join(decomp)


s = "()()"
print(removeOuterParentheses(s))
