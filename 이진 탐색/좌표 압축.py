n = int(input())
data = list(map(int, input().split()))
array = list(set(data[:]))
array.sort()


def lower_idx(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start


for i in data:
    print(lower_idx(array, i, 0, len(array) - 1))
