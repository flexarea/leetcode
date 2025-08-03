def maxProfit(prices):
    if len(prices) <= 1:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i]-prices[i-1])
    return profit


print(maxProfit([1, 2, 3, 4, 5]))
