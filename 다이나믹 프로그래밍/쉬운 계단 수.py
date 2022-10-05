N = int(input())

# DPtable 초기화
dp = [[0] * 10 for _ in range(N + 1)]

# 1층 초값 설정
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 점화식 구현
for n in range(2, N + 1):
    dp[n][0] = dp[n - 1][1]  # 끝자리가 0
    dp[n][9] = dp[n - 1][8]  # 끝자리가 9

    for k in range(1, 9):  # 끝자리가 1~8 -> 전 자리수가 k-1, k+1일 때의 경우의 수의 합
        dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k + 1]

print(sum(dp[N]) % 1000000000)
