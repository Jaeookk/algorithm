n, k = map(int, input().split())  # n은 물품의 수, k는 배낭 최대 무게
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

# dp[n][k] = n번째 물건 까지 살펴봤을 때, 무게가 k인 배낭의 최대 가치
# 점화식
# 새로 넣을 물건이 배낭의 허용 무게를 넘긴다면 : dp[i][j] = dp[i-1][j]
# 아니라면 : dp[i][j] = max(d[i-1][j-weight] + value, d[i-1][j])
# value , weight = i번째 물건의 가치와 무게

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = arr[i][0]
        value = arr[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

print(max(dp[-1]))
