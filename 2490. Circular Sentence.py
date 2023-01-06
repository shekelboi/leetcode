def isCircularSentence(sentence):
    words = sentence.split()
    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0]:
            return False
    if words[0][0] != words[-1][-1]:
        return False
    return True


sentence = "leetcode exercises sound delightful"
print(isCircularSentence(sentence))
