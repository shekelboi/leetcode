def findContentChildren(g, s):
    g.sort(reverse=True)
    s.sort(reverse=True)

    g_index = 0
    s_index = 0

    result = 0

    while g_index < len(g) and s_index < len(s):
        if g[g_index] <= s[s_index]:
            result += 1
            s_index += 1
        g_index += 1

    return result


g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
print(findContentChildren(g, s))
