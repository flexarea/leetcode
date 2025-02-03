def maxProfit(prices):
    if len(prices) <= 1:
        return prices[0]
    l, r = 0, 1

    max_p = 0
    while r < len(prices):
        if prices[l] > prices[r]:
            l = r
            r += 1
        else:
            max_p = max(max_p, prices[r]-prices[l])
            r += 1
    return max_p


print(maxProfit([7, 1, 5, 3, 6, 4]))
