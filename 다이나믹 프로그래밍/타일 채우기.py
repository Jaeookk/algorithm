n = int(input())

dp = [0] * (n + 1)

if n < 2:
    print(dp[n])
else:
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum(dp[: i - 3] * 2) + 2

    print(dp[-1])
