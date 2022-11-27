def maxNumberOfBalloons(text):
    balloon = {
        "b": 1,
        "a": 1,
        "l": 2,
        "o": 2,
        "n": 1
    }

    return min([text.count(key) // value for (key, value) in balloon.items()])


text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))
