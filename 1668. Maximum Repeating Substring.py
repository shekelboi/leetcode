def maxRepeating(sequence, word):
    current_sequence = 0
    longest_sequence = 0
    start_index = 0
    index = 0

    counter = 0

    while counter < len(sequence):
        print(counter)
        if index == len(word):
            index = 0
            current_sequence += 1
            longest_sequence = max(longest_sequence, current_sequence)

        if word[index] == sequence[counter]:
            if index == 0 and current_sequence == 0:
                start_index = counter
            index += 1
        else:
            counter = start_index + 1
            index = 0
            current_sequence = 0
        counter += 1

    return longest_sequence


sequence = "ababacbababa"
word = "ba"
print(maxRepeating(sequence, word))
