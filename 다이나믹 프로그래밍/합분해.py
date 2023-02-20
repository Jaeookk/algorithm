n, k = map(int, input().split())

dp = [[0] * 201 for _ in range(201)]
# dp[n][k] = 0 ~ n 수 에서 k개를 사용하여 n을 만들 수 있는 경우의 수
# 점화식 : dp[n][k] = dp[n-1][k] + dp[n][k-1]
# dp[0][1:] = 1

for i in range(1, k + 1):
    dp[0][i] = 1
  
for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000
        
print(dp[n][k])
