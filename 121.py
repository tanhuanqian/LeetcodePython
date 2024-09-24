def maxProfit(prices):
    minimum = float('inf')
    maximum = 0
    for price in prices:
        if price < minimum:
            minimum = price
        elif price - minimum > maximum:
            maximum = price-minimum
        print(minimum, maximum)
    return maximum

prices = [7,1,5,3,6,4]
print(maxProfit(prices))