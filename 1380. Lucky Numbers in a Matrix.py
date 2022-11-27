def luckyNumbers(matrix):
    lucky_numbers = []
    for row in matrix:
        min_num = min(row)
        index = row.index(min_num)
        max_num = min_num
        for r in matrix:
            if r[index] > max_num:
                max_num = r[index]
                break
        if max_num == min_num:
            lucky_numbers.append(min_num)
    return lucky_numbers


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
print(luckyNumbers(matrix))
