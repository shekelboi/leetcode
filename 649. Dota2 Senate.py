def predictPartyVictory(senate: str) -> str:
    def is_unique(arr):
        s = set()
        for n in arr:
            s.add(n)
            if len(s) > 1:
                return False
        return True

    l = list(senate)

    def last_index(arr, text):
        for i in reversed(range(len(arr))):
            if arr[i] == text:
                return i
        return -1

    while not is_unique(l):
        counter = 0
        print(l)
        while counter < len(l):
            remove_this = ''
            if l[counter] == 'D':
                remove_this = 'R'
            else:
                remove_this = 'D'
            print(remove_this)
            if remove_this in l:
                index = last_index(l, remove_this)
                l = l[:index] + l[index + 1:]
            counter += 1
    return 'Radiant' if l[0] == 'R' else 'Dire'


inp = 'DRDRR'
print(predictPartyVictory(inp))
