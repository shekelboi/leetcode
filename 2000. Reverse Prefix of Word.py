def reversePrefix(word, ch):
    index = word.find(ch)
    if index == -1:
        return word
    return word[index::-1] + word[index + 1::]


word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))
