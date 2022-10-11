#      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1원  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 5원            1 2 3 4 5 2  3  4  5  6  3
# 12원                           1  2  3  4

# (i에서 현재 코인 값을 빼주었을 때의 코인 사용 개수 + 지금 코인 개수 하나) 와
# (이전 코인들로만 조합했을 때 사용된 코인 개수)를 비교하여 더 작은 값을 dp배열에 담는다.
# dp[i] = min(dp[i],dp[i-coin]+1)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
