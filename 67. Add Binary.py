def addBinary(a, b):
    result = []
    max_length = max(len(a), len(b))
    remainder = 0

    for i in range(max_length):
        current_result = remainder
        a_index = len(a) - 1 - i
        b_index = len(b) - 1 - i
        if a_index >= 0:
            current_result += int(a[a_index])
        if b_index >= 0:
            current_result += int(b[b_index])
        if current_result == 2:
            current_result = 0
            remainder = 1
        elif current_result == 3:
            current_result = 1
            remainder = 1
        else:
            remainder = 0
        result.insert(0, str(current_result))

    if remainder > 0:
        result.insert(0, str(remainder))

    return "".join(result)


a = "11"
b = "1"
print(addBinary(a, b))
