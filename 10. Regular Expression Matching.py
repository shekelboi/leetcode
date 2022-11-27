def isMatch(s, p):
    expressions = []
    for c in p:
        if c.isalpha() or c == ".":
            expressions.append([c])
        else:
            expressions[-1].append(c)

    counter = 0
    lastStarPosition = None
    while len(expressions) > 0:
        # If the counter reached the end of the word, reset it to end of the word
        if counter == len(s):
            counter = len(s) - 1

        currentExpression = expressions.pop(0)
        if len(currentExpression) > 1:
            lastStarPosition = counter
            while counter < len(s) and (s[counter] == currentExpression[0] or currentExpression[0] == "."):
                # and currentExpression[1] == "*" but it can be omitted
                counter += 1
            else:
                match = s[lastStarPosition:counter]
                if len(match) == 0:
                    continue

                singular_expressions = []
                while len(expressions) > 0 and len(expressions[0]) == 1:  # As long as the first expression is singular
                    if expressions[0][0] == match[0]:
                        singular_expressions.append(expressions.pop(0))
                    else:
                        break

                # If there are no singular expressions
                if len(singular_expressions) == 0:
                    continue
                # If there are more expressions than the length of the match
                # or if the singular expressions do not match with the string
                if len(singular_expressions) > counter or match[counter - len(singular_expressions):counter] != "".join(
                        [e[0] for e in singular_expressions if e[0] == match[0]]):
                    return False
                continue
        else:
            if s[counter] == currentExpression[0] or currentExpression[0] == ".":
                counter += 1
            else:
                if lastStarPosition is not None:
                    for i in range(lastStarPosition, counter):
                        if s[i] == currentExpression[0]:
                            lastStarPosition = None
                            break
                break
    return counter >= len(s) and len([e for e in expressions if len(e) == 1]) == 0


s = "aaa"
p = "ab*a*c*a"
print(isMatch(s, p))

# Some examples to consider:
# s = "aaa" and p = "a*a" -> meaning that the expression following * must also be considered
# Long input:
# s = "aaa" and p = "aaaa" -> if there are more alphanumeric characters not followed by star
# than the length of the input it will automatically fail

# aaa
# ab*a*ac*a
# true
