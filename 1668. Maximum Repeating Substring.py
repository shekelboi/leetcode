def maxRepeating(sequence, word):
    longest_sequence = 0
    for i in range(len(word)):
        current_sequence = 0
        for j in range(i, len(sequence), len(word)):
            for k in range(len(word)):
                if (j + k) >= len(sequence) or word[k] != sequence[j + k]:
                    current_sequence = 0
                    break
                current_sequence += 1
                longest_sequence = max(current_sequence, longest_sequence)

    return longest_sequence // len(word)


sequence = "bacacbc"
word = "cba"
print(maxRepeating(sequence, word))
