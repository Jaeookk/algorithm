n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = board[0][0]

for col in range(1, m):
    dp[0][col] = board[0][col] + dp[0][col - 1]

for row in range(1, n):
    dp[row][0] = board[row][0] + dp[row - 1][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = board[i][j] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[n - 1][m - 1])
