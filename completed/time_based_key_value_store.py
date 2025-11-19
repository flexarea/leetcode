class TimeMap:

    def __init__(self):
        self.time_dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_dic:
            self.time_dic[key].append((timestamp, value))
        else:
            self.time_dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_dic:
            return ""

        timestamp_arr = self.time_dic[key]
        low, high = 0, len(timestamp_arr) - 1
        mid = 0
        ans = ""

        while low <= high:
            mid = (low+high) // 2
            if timestamp_arr[mid][0] == timestamp:
                return timestamp_arr[mid][1]
            if timestamp_arr[mid][0] < timestamp:
                ans = timestamp_arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
