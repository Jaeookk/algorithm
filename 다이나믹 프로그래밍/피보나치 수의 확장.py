n = int(input())

if n >= 0:
    dp = [0] * (n + 2)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
else:
    dp = [0] * (abs(n) + 2)
    dp[1] = 1
    for i in range(-1, n - 1, -1):
        temp = dp[i + 2] - dp[i + 1]
        if temp < 0:
            dp[i] = -(abs(temp) % 1000000000)
        else:
            dp[i] = temp % 1000000000

if dp[n] > 0:
    print(1)
    print(abs(dp[n]))
elif dp[n] == 0:
    print(0)
    print(0)
else:
    print(-1)
    print(abs(dp[n]))
