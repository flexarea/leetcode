# return index of x if x exist in arr
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        # compute mid
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

        # not found
    return -1


arr = [2, 3, 4, 10, 40]
x = 10

print(binarySearch(arr, x))
