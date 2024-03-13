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
    find_possibilities(l.copy(), 0, possibilities)

    print('Pos:')
    print(possibilities)

    # Check all the possibilities
    # If there is a possibility that the first party wins, return with that party
    # Otherwise return with the other party
    return 'Radiant' if possibilities[0] == 'R' else 'Dire'


def find_possibilities(l, position, possibilities):
    if is_unique(l):
        possibilities.append(l[0])
        return
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
            find_possibilities(c, next_pos, possibilities)


# inp = 'DRDRR'
inp = 'RRRDDD'
print(predictPartyVictory(inp))
