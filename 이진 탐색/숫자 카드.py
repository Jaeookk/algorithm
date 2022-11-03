n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
data = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for x in data:
    print(binary_search(array, x, 0, n - 1), end=" ")
