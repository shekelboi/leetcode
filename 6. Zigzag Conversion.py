# Length of the sequence (s) is 2+(n-2)*2 where n is the number of rows
# Within the sequence:
# First row is always 0
# Last row is always n-1
# The rows in between are always i and s/2-i+s


def convert(s, numRows):
    if numRows == 1:
        return s
    arr = [[] for i in range(numRows)]
    sequence_length = 2 + (numRows - 2) * 2
    for i in range(len(s)):
        if i % sequence_length == 0:
            arr[0].append(s[i])
        elif i % (numRows - 1) == 0:
            arr[-1].append(s[i])
        else:
            current_row = i % sequence_length
            if current_row >= numRows:
                current_row = (numRows - 1) - abs(current_row - (numRows - 1))
            arr[current_row].append(s[i])
    return "".join(["".join(a) for a in arr])


s = "PAYPALISHIRING"
print(convert(s, 4))
