def maxArea(height):
    pointer1 = 0
    pointer2 = len(height) - 1
    max_area = 0
    while pointer1 != pointer2:
        area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1)
        if height[pointer1] > height[pointer2]:
            pointer2 -= 1
        else:
            pointer1 += 1

        if area > max_area:
            print(f"{height[pointer1]} {height[pointer2]}, {pointer2 - pointer1}")
            max_area = area
    return max_area


height = [1, 9, 1, 9, 1]
print(maxArea(height))
