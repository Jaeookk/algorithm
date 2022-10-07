# 시간초과
# import sys

# sys.setrecursionlimit(10000001)
# n = int(sys.stdin.readline())
# d = [0] * 10000001
# d[1] = 1
# d[2] = 2
# d[3] = 4

# for _ in range(n):
#     x = int(input())
#     if x < 4:
#         print(d[x])
#         continue
#     for i in range(4, x + 1):
#         d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009
#     print(d[x])

import sys

input = sys.stdin.readline

dp = [0 for i in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n] % 1000000009)
