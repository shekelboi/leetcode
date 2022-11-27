def floodFill(image, sr, sc, color):
    original_value = image[sr][sc]
    length_row = len(image)
    length_col = len(image[0])
    if image[sr][sc] == color:
        return image

    flood(image, sr, sc, color, length_row, length_col, original_value)
    return image


def flood(image, sr, sc, color, length_row, length_col, original_value):
    print(image)
    if image[sr][sc] == original_value:
        image[sr][sc] = color
        if sr + 1 < length_row:  # down
            flood(image, sr + 1, sc, color, length_row, length_col, original_value)
        if sr - 1 >= 0:  # up
            flood(image, sr - 1, sc, color, length_row, length_col, original_value)
        if sc + 1 < length_col:  # right
            flood(image, sr, sc + 1, color, length_row, length_col, original_value)
        if sc - 1 >= 0:  # left
            flood(image, sr, sc - 1, color, length_row, length_col, original_value)


print("OK")
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))
