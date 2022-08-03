n = int(input())

array = [()]
for i in range(n):
    T, P = map(int, input().split())
    array.append((T, P))

# dp[i] = (마지막 날 부터)i번째 날 까지 일을 했을 때, 최적의 해
dp = [0] * (n + 2)

for i in range(n, 0, -1):
    if array[i][0] + i <= n + 1:  # 날짜를 초과하지 않으면
        # i번째 날은 (i + 1번째 날 최적의 해)와 (i번째 수익 + T_i 만큼 지난 후 수익) 중에서 큰 값
        dp[i] = max(dp[i + 1], array[i][1] + dp[i + array[i][0]])
    else:  # 날짜를 초과하면
        dp[i] = dp[i + 1]

print(max(dp))
