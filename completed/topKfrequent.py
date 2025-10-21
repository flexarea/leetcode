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


# progress?
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        dic = Counter(nums)
        sorted_dic = dict(
            sorted(dic.items(), key=lambda item: item[1], reverse=True)).keys()
        return list(sorted_dic)[:k]
