# 파라메트릭 서치
m, n = map(int, input().split())

snacks = list(map(int, input().split()))


def binary_search(arr, start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in arr:
            if i >= mid:
                cnt += i // mid
        if cnt >= m:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res


print(binary_search(snacks, 1, max(snacks)))
