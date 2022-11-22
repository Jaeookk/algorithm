import sys


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

min_value = sys.maxsize
end = 0

for start in range(n):
    while end < n and (arr[end] - arr[start] < m):
        end += 1
    if end == n:
        break
    min_value = min(min_value, arr[end] - arr[start])

print(min_value)
