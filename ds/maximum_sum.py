def maximum_sum(arr, k):
    max_sum = -100000000

    n = len(arr)
    windonw_sum = sum(arr[:k])

    for i in range(n-k):
        windonw_sum = windonw_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, windonw_sum)
    return max_sum


print(maximum_sum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
