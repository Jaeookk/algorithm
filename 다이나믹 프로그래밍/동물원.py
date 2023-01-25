n = int(input())
dp = [[0] * 3 for i in range(100001)]
# [i][0]은 왼쪽, [i][1]은 오른쪽, [i][2]은 둘다 빈

for i in range(3):
    dp[1][i] = 1
for i in range(2, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
print(sum(dp[n]) % 9901)
