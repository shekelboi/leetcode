def numWaterBottles(numBottles, numExchange):
    result = numBottles
    while numBottles // numExchange > 0:
        new_bottles = numBottles // numExchange
        result += new_bottles
        remainder = numBottles % numExchange
        numBottles = new_bottles + remainder
    return result


numBottles = 9
numExchange = 3
print(numWaterBottles(numBottles, numExchange))
