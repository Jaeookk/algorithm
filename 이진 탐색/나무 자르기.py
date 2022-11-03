n, m = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in arr:
            if i >= mid:
                count += i - mid
        if count >= target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res


print(binary_search(trees, m, 0, trees[-1]))
