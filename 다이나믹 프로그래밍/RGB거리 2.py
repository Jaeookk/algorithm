n = int(input())
money = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

INF = 10000001
answer = INF

for T in range(3):
    dp = [[INF, INF, INF] for _ in range(n + 1)]
    dp[1][T] = money[1][T]

    for j in range(2, n + 1):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + money[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + money[j][1]
        dp[j][2] = min(dp[j - 1][1], dp[j - 1][0]) + money[j][2]

    temp = min(dp[n][T - 1], dp[n][T - 2])
    answer = min(answer, temp)

print(answer)
