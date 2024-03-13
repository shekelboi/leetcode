def find_words(words):
    rows = [set(s) for s in ["qwertyuiop", "asdfghjkl", "zxcvbnm"]]

    def contained_in(letter, rows):
        return next(i for i, r in enumerate(rows) if letter in r)

    def can_be_written(word, rows):
        first_letter = word[0]
        row_number = contained_in(first_letter, rows)
        if row_number is None:
            return False
        charset = rows[row_number]

        for l in word:
            if l not in charset:
                return False
        return True

    return [w for w in words if can_be_written(w.lower(), rows)]


words = ["Hello", "Alaska", "Dad", "Peace"]
print(find_words(words))
