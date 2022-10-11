# 1. 가장 작은 가치의 동전으로 k원을 만들 수 있는 경우의 수를 구한다.
# 2. 그 다음 동전으로 경우의 수를 구해야 하는데, 만약 k-coin을 만들 수 있다면 -> k원을 만들 수 있다.
# 즉, dp[i] 를 i원을 만드는 경우의 수라고 하면
# dp[i] += dp[i-coin] 이다. 이미 구한 작은 가치의 화폐의 경우의 수에 그 이후의 가치의 화폐의 경우의수를 더한다.

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]
print(dp[k])
