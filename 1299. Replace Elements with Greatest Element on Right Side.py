def replaceElements(arr):
    index = len(arr) - 1
    max_num = -1

    while 0 <= index:
        previous = arr[index]
        arr[index] = max_num
        max_num = max(previous, max_num)
        index -= 1
    return arr


arr = [400]
print(replaceElements(arr))
