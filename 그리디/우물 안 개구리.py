# 소프티어 레벨 3
import sys


input = sys.stdin.readline

n, m = map(int, input().split())
weight = [0] + list(map(int, input().split()))
check = [True] * (n + 1)
check[0] = False

for _ in range(m):
    i, j = map(int, input().split())
    if weight[i] < weight[j]:
        check[i] = False
    elif weight[i] > weight[j]:
        check[j] = False
    else:
        check[i] = False
        check[j] = False

print(check.count(True))
