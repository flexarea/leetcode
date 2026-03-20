"""
Example: Given an array of distinct integer values, count the number of pairs of integers that
have difference k. For example, given the array { 1, 7, 5, 9, 2, 12, 3} and the difference
k = 2,there are four pairs with difference2: (1, 3), (3, 5), (5, 7), (7, 9).
"""


def fn(arr, k):
    seen = {val for val in arr}
    res = []

    for val in seen:
        if (val+k) in seen:
            res.append((val, val+k))
    return res


print(fn([1, 7, 5, 9, 2, 12, 3], 2))
