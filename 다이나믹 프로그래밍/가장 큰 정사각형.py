# 1 1 1 1    1 1 1 1
# 1 1 1 1    1 4 4 4
# 1 1 1 1    1 4 9 9
# 1 1 1 1    1 4 9 16

# 1 1 1 0    1 1 1 0
# 1 1 1 1    1 4 4 1
# 1 1 1 1    1 4 9 4
# 1 1 1 1    1 4 9 9

# dp[i][j] = i,j일때 만들 수 있는 최대 정사각형 넓이
# 점화식
# dp[i][j] != 0 이고
# dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1] 모두 0이 아니면
# dp[i][j] 는 위 세개의 값중 최소값보다 변이 1 더 큰 정사각형 넓이가 된다.


n, m = map(int, input().split())

dp = [[0] * (m + 1)]
for _ in range(n):
    temp = [0] + list(map(int, input()))
    dp.append(temp)
#
# print(dp)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (
            dp[i][j] != 0
            and dp[i - 1][j - 1] != 0
            and dp[i - 1][j] != 0
            and dp[i][j - 1] != 0
        ):
            value = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            dp[i][j] = int((value ** (1 / 2) + 1) ** 2)

# print(dp)
result = 0
for k in range(1, n + 1):
    tmp = max(dp[k])
    result = max(result, tmp)
print(result)
