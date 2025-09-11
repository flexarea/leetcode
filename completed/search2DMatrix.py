class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            low = 0
            high = len(arr)-1
            mid = 0

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] == target:
                    return True
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        for i in matrix:
            if binary_search(i, target):
                return True
        return False
