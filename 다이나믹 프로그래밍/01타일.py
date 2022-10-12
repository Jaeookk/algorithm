# 점화식 dp[i] = dp[i-1] + dp[i-2]
n = int(input())

dp = [1] * (n + 1)

if n < 2:
    print(dp[n])
else:
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    print(dp[n])
