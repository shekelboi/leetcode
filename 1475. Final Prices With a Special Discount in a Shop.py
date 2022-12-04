def finalPrices(prices):
    def min_index(current_index, arr):
        for i in range(current_index + 1, len(arr)):
            if prices[i] <= arr[current_index]:
                return i
        return -1

    for i, price in enumerate(prices):
        if min_index(i, prices) != -1:
            prices[i] = prices[i] - prices[min_index(i, prices)]

    return prices


prices = [8, 4, 6, 2, 3]
print(finalPrices(prices))
