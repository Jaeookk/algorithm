from collections import defaultdict


def solution(n, k, arr):
    start, end = 0, 0
    count = defaultdict(int)
    answer = 0
    while end < n:
        if count[arr[end]] >= k:
            count[arr[start]] -= 1
            start += 1
        else:
            count[arr[end]] += 1
            end += 1
            answer = max(answer, end - start)
    return answer


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(n, k, arr))
