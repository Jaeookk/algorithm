import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

_sum = sum(arr[:k])
answer = _sum

for end in range(k, n):
    _sum = _sum - arr[end - k] + arr[end]
    answer = max(answer, _sum)
print(answer)
