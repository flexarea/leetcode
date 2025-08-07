def topKFrequent(nums, k):
    count = {key: 0 for key in set(nums)}
    freq = []
    for i in nums:
        count[i] += 1

    sorted_nums = sorted(
        count.items(), key=lambda item: item[1], reverse=True)
    for i in range(k):
        freq.append(sorted_nums[i][0])
    return freq


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
