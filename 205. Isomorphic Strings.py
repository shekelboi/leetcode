def isIsomorphic(s: str, t: str) -> bool:
    char_A = ord('A')

    inputs = [s, t]
    patterns = []

    for inp in inputs:
        pattern_dict = dict()
        counter = 0
        pattern = ""
        for c in inp:
            if c in pattern_dict:
                pattern += pattern_dict[c]
            else:
                new_symbol = chr(char_A + counter)
                pattern_dict[c] = new_symbol
                pattern += new_symbol
                counter += 1
        patterns.append(pattern)

    return patterns[0] == patterns[1]


s = "egg"
t = "add"

print(isIsomorphic(s, t))