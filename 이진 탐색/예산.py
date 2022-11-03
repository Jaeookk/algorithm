n = int(input())
budget = list(map(int, input().split()))
budget.sort()

m = int(input())


def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in arr:
            if i > mid:
                cnt += mid
            else:
                cnt += i
        if cnt <= target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    return res


if sum(budget) <= m:
    print(budget[-1])
else:
    print(binary_search(budget, m, 0, budget[-1]))
