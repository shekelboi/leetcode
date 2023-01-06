def oddString(words):
    for i in range(1, len(words[0])):
        occurences = []
        for j, word in enumerate(words):
            diff = ord(word[i]) - ord(word[i - 1])
            found = False
            for o in occurences:
                if o[0] == diff:
                    o[1] += 1
                    found = True
            if not found:
                occurences.append([diff, 1, j])

        for o in occurences:
            if o[1] == 1:
                return words[o[2]]


words = ["adc", "wzy", "abc"]
print(oddString(words))
