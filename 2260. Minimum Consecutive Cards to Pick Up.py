def minimumCardPickup(cards):
    card_dict = {}
    min_diff = -1
    for i, c in enumerate(cards):
        if c in card_dict:
            difference = i - card_dict[c] + 1
            if difference < min_diff or min_diff == -1:
                min_diff = difference
        card_dict[c] = i
    return min_diff


cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))
