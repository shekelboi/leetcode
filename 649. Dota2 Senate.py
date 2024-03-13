def is_unique(arr):
    s = set()
    for n in arr:
        s.add(n)
        if len(s) > 1:
            return False
    return True


def predictPartyVictory(senate):
    l = list(senate)
    possibilities = []
    res = find_possibilities(l[0], l.copy(), 0, possibilities)

    # print('RES', res)
    # print('Pos:')
    # print(possibilities)

    # Check all the possibilities
    # If there is a possibility that the first party wins, return with that party
    # Otherwise return with the other party
    d = {
        'D': 'Dire',
        'R': 'Radiant'
    }
    opp = {
        'R': 'Dire',
        'D': 'Radiant'
    }
    return d[l[0]] if res else opp[l[0]]


def find_possibilities(original, l, position, possibilities):
    if is_unique(l):
        possibilities.append(l[0])
        if l[0] == original:
            return True
    if position >= len(l):
        position = 0

    for i in range(len(l)):
        # If different from the current one, it will be removed
        if l[i] != l[position]:
            c = l[:i] + l[i + 1:]
            if i <= position:
                next_pos = position
            else:
                next_pos = position + 1
            return find_possibilities(original, c, next_pos, possibilities)


# inp = 'DRDRR'
inp = 'DRRDRDRDRDDRDRDR'
print(predictPartyVictory(inp))
