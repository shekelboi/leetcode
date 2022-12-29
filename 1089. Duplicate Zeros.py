def duplicateZeros(arr):
    counter = 0
    while counter < len(arr):
        if arr[counter] == 0:
            arr.insert(counter, 0)
            arr.pop()
            counter += 1
        counter += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
print(duplicateZeros(arr))
print(arr)
