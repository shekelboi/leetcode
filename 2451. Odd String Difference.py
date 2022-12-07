def oddString(words):
    difference_arr = []
    for word in words:
        difference = []
        for i in range(1, len(words[0])):
            difference.append(ord(word[i]) - ord(word[i - 1]))
        difference_arr.append(tuple(difference))

    occurences = {}
    for diff in difference_arr:
        if diff not in occurences:
            occurences[diff] = 1
        else:
            occurences[diff] += 1

    unique = [k for (k, v) in occurences.items() if v == 1][0]
    return words[difference_arr.index(unique)]


words = ["adc", "wzy", "abc"]
print(oddString(words))
