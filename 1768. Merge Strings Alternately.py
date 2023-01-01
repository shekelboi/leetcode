def mergeAlternately(word1, word2):
    counter = 0
    merged = ""

    while counter < max(len(word1), len(word2)):
        if counter < len(word1):
            merged += word1[counter]
        if counter < len(word2):
            merged += word2[counter]
        counter += 1

    return merged


word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
