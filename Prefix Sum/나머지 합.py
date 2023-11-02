import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
tmp = 0
d = defaultdict(int)

for i in range(n):
    tmp = (arr[i] + tmp) % m
    d[tmp] += 1

for i in range(m):
    if i == 0:
        result += d[i]
    if d[i] != 0:
        result += d[i] * (d[i] - 1) // 2

print(result)
